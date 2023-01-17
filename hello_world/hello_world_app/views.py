from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, generate_slug_hash
from .forms import CreateMemberForm, UpdateMemberForm

def generate_slug(firstname, lastname, slug_hash):
  return f"{firstname}-{lastname}-{slug_hash}".lower().replace(" ", "")
      

def hello_world(request):
    template = loader.get_template("hello_world.html")
    return HttpResponse(template.render())

def create_member(request):
  msg, error = None, None
  if request.method == 'POST':
    form = CreateMemberForm(request.POST)
    if form.is_valid():
      member = form.save(commit=False) #commit = False porque no lo queremos guardar todavía
      member.slug_hash = generate_slug_hash()
      member.slug = generate_slug(member.firstname, member.lastname, member.slug_hash)
      member.save()
      msg = "Member created!"

    else:
      error = 'Form invalid'
    
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
    context = {
      'msg': msg,
    }
    return render(request, 'delete_member.html', context)
  

def all_members(request):
  my_members = Member.objects.all().values()
  context = {
    'my_members': my_members,
  }
  return render(request, 'all_members.html', context)

def member(request, slug):
  my_member = get_object_or_404(Member, slug=slug)
  context = {
    'my_member': my_member,
  }
  
  return render(request, 'member.html', context)

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
