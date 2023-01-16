from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member, generate_slug_hash, get_time_today
from .forms import CreateMemberForm, UpdateMemberForm

def hello_world(request):
    template = loader.get_template("hello_world.html")
    return HttpResponse(template.render())

def create_member(request):
  msg, error = None, None
  if request.method == 'POST':
    form = CreateMemberForm(request.POST)
    if form.is_valid():
      member = form.save(commit=False) #commit = False porque no lo queremos guardar todavía
      member.joined_date = get_time_today()
      member.slug_hash = generate_slug_hash()
      member.slug = f"{member.firstname}-{member.lastname}-{generate_slug_hash()}"
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
  if request.method == 'PUT':
    form = UpdateMemberForm(request.PUT)
    if form.is_valid():
      member = form.save(commit=False)
      #member.slug_hash = generate_slug_hash()
      #member.slug = f"{member.firstname}-{member.lastname}-{generate_slug_hash()}"
      member.save()
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
