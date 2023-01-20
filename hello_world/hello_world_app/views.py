from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Member, generate_slug_hash
from .forms import CreateMemberForm, UpdateMemberForm

def generate_slug(firstname, lastname, slug_hash):
  return f"{firstname}-{lastname}-{slug_hash}".lower().replace(" ", "")
      
def create_member(request):
  msg, error = None, None
  if request.method == 'POST':
    form = CreateMemberForm(request.POST)

    title = "Create member"
    if form.is_valid():
      member = form.save(commit=False) #commit = False porque no lo queremos guardar todavía
      member.slug_hash = generate_slug_hash()
      member.slug = generate_slug(member.firstname, member.lastname, member.slug_hash)
      member.save()
      msg = "Member created!"
      # redirect('hello_world:success', msg = msg)
      return render(request, 'success.html',  {'msg': msg, 'title': title})

    else:
      error = 'Form invalid'
      # redirect('hello_world:success', msg = msg)
      return render(request, 'failure.html',  {'error': error, 'title': title})
    
  elif request.method == 'GET':     
      form = CreateMemberForm()

  context = {
    'form': form,
    'msg' : msg,
    'error' :error
  }
  return render(request, 'create_member.html', context)

def update_member(request, slug):
  msg, error = None, None

  my_member = Member.objects.get(slug=slug)
  if request.method == 'POST':
    form = UpdateMemberForm(request.POST)
    if form.is_valid():
      for field in form.cleaned_data:
        if form.cleaned_data[field]:
          setattr(my_member, field, form.cleaned_data[field])
          
      slug_hash = slug[slug.rfind("-")+1:]
      my_member.slug = generate_slug(my_member.firstname, my_member.lastname, slug_hash)
      my_member.save()
      msg = "Member updated!"
      context = {
          'my_member': my_member,
          'form': form,
          'msg' : msg,
          'error' :error
          }
      title = 'Update member'
      return render(request, 'success.html',  {'msg': msg, 'title': title})
    else:
      error = 'Form invalid'
    
  elif request.method == 'GET':     
    form = UpdateMemberForm()

  context = {
    'my_member': my_member,
    'form': form,
    'msg' : msg,
    'error' :error
  }
  return render(request, 'update_member.html', context)

def delete_member(request, slug):
  my_member = get_object_or_404(Member, slug=slug)
  if request.method == 'GET':
    context = {
      'my_member': my_member,
    }
    return render(request, 'delete_member.html', context)
  elif request.method == 'POST':
    my_member.delete()
    msg = f'{my_member} Deleted.'
    title = "Delete member"
    # redirect('hello_world:success', msg = msg)
    return render(request, 'success.html',  {'msg': msg, 'title': title})
    #return HttpResponseRedirect(reverse('hello_world:delete_member', wargs={'msg': msg}))

class MemberDeleteView(generic.DeleteView):
  model = Member
  template_name = "delete_member.html"
  success_url = reverse_lazy('hello_world:success')
  context_object_name = 'my_member'
  success_message = "%(name)s was created successfully"

  def get_object(self):
    self.member = get_object_or_404(Member, slug=self.kwargs['slug'])
    return self.member

  def get_success_message(self, cleaned_data):
      msg = self.success_message % dict(
        cleaned_data,
        name=self.object.__str__(),
        )
      return msg

  '''
  def delete(self, *args, **kwargs):
    self.object = self.get_object()
    super().delete(*args, **kwargs)

  def get_success_url(self):
    return reverse_lazy('hello_world:detail_member', kwargs={'slug': self.object.slug})
  '''
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

class MainView(generic.TemplateView):
  template_name = "main.html"

class HelloWorldView(generic.TemplateView):
  template_name = "hello_world.html"

  ''' Si quieres pasarle algún atributo en el contexto debes definir el método get

  def get(self, request, *args, **kwargs):
    context = {msg : 'Mi mensaje'}
    return render(request, self.template_name, context)
  
  '''