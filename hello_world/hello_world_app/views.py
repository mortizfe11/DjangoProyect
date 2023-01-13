#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def hello_world(request):
    template = loader.get_template("hello_world.html")
    return HttpResponse(template.render())
    #return HttpResponse("Hello world!")


def all_members(request):
  my_members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'my_members': my_members,
  }
  return HttpResponse(template.render(context, request))

def member(request, id):
  if id > 0 and isinstance(id, int):
    try:
      my_member = Member.objects.get(id=id)
      template = loader.get_template('member.html')
      context = {
        'my_member': my_member,
      }
      return HttpResponse(template.render(context, request))

    except:
      return HttpResponse(f"Error detected")
 
  else:
    return HttpResponse(f"The number {id} is incorrect.")
  

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())