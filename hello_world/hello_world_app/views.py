from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member, generate_slug_hash, get_time_today
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
      '''firstname, lastname, phone = form.cleaned_data.values()

      if firstname != my_member.firstname and firstname != '':
        my_member.firstname = firstname
      if lastname != my_member.lastname and lastname != '':
        my_member.lastname = lastname
      if phone != my_member.phone and phone != '':
        my_member.phone = phone
      '''
      for field in form.cleaned_data:
        setattr(my_member, field, form.cleaned_data[field])
      #print(member, my_member.slugh_hash)
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
  my_member = Member.objects.get(slug=slug)
  if request.method == 'GET':
    template = loader.get_template('delete_member.html')
    context = {
      'my_member': my_member,
    }
    return HttpResponse(template.render(context, request))
  elif request.method == 'POST':
    my_member.delete()
    template = loader.get_template('delete_member.html')
    msg = f'{my_member} Deleted.'
    context = {
      'msg': msg,
    }
    return HttpResponse(template.render(context, request))
  

def all_members(request):
  my_members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'my_members': my_members,
  }
  return HttpResponse(template.render(context, request))

def member(request, slug):
  my_member = Member.objects.get(slug=slug)
  template = loader.get_template('member.html')
  context = {
    'my_member': my_member,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
