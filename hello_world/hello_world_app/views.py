from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Member, generate_slug_hash
from .forms import CreateMemberForm, UpdateMemberForm

class MyView(generic.TemplateView):
  pass

class AllMembersView(generic.ListView):
  template_name = 'all_members.html'
  context_object_name = "my_members"

  def get_queryset(self):
    return Member.objects.all().values()

class MemberView(generic.DetailView):
  template_name = 'member.html'
  context_object_name = "my_member"

  def get_object(self):
    self.member = get_object_or_404(Member, slug=self.kwargs['slug'])
    return self.member


def generate_slug(firstname, lastname, slug_hash):
  return f"{firstname}-{lastname}-{slug_hash}".lower().replace(" ", "")

class CreateMemberView(generic.CreateView):
    template_name = "create_member.html"
    form_class = CreateMemberForm
    
    def post(self, request, *args, **kwargs):
      form = self.form_class(request.POST)
      if form.is_valid():
        member = form.save(commit=False) #commit = False porque no lo queremos guardar todavía
        member.slug_hash = generate_slug_hash()
        member.slug = generate_slug(member.firstname, member.lastname, member.slug_hash)
        member.save()
        messages.success(request, f"{member} was created successfully")
      else:
        messages.warning(request, 'Form invalid.')
      return redirect(reverse('hello_world:all_members'))

class UpdateMemberView(generic.UpdateView):
    model = Member
    template_name = "update_member.html"
    form_class = UpdateMemberForm
    context_object_name = 'member'

    def get_queryset(self):
      return Member.objects.filter(slug=self.kwargs['slug'])

    def post(self, request, *args, **kwargs):
      slug = self.kwargs['slug']
      member = get_object_or_404(Member, slug=slug)
      form = self.form_class(request.POST)
      if form.is_valid():
        for field in form.cleaned_data:
          if form.cleaned_data[field]:
            setattr(member, field, form.cleaned_data[field])
            
        slug_hash = slug[slug.rfind("-")+1:]
        member.slug = generate_slug(member.firstname, member.lastname, slug_hash)
        member.save()
        messages.success(request, f"{member} was updated successfully")
      else:
        messages.warning(request, 'Form invalid.')
      return redirect(reverse('hello_world:all_members'))

class MemberDeleteView(SuccessMessageMixin,generic.DeleteView):
  model = Member
  template_name = "delete_member.html"
  success_url = reverse_lazy('hello_world:all_members')
  context_object_name = 'my_member'

  def get(self, request, *args, **kwargs):
    my_object = self.get_object()
    messages.success(request, f"{my_object} was deleted successfully")
    return super().get(request, *args, **kwargs)

main_page = MyView.as_view(template_name = "main.html")
hello_world_page = MyView.as_view(template_name = "hello_world.html")
all_members_page = AllMembersView.as_view()
detail_member_page = MemberView.as_view()
create_member_page = CreateMemberView.as_view()
update_member_page = UpdateMemberView.as_view()
delete_member_page = MemberDeleteView.as_view()