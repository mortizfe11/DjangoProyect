from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View, generic
from django.contrib import messages

from .forms import CreateAnimalForm
from .models import Animal, Publisher

# Create your views here.

class SucessView(generic.TemplateView):
    template_name = 'class_basics/success.html'

    def get(self, request):
        storage = messages.get_messages(request)
        messageList = [message.message for message in storage]
        return render(request, self.template_name, { 'messages':  messageList})

class IndexView(generic.TemplateView):
    template_name = 'class_basics/index.html'

class AnimalListView(generic.ListView):
    model = Animal
    template_name = 'class_basics/animal.html'
    context_object_name = "animals"

    def get_queryset(self):
        return Animal.objects.all().values()

class AnimalView(View):
    animal = 'animal'
    sound = "Sound of animal"

    def get(self, request):
        return HttpResponse(f"{self.animal}: {self.sound}")

class CatView(AnimalView):
    animal = 'cat'
    sound = 'miau'

class DogView(AnimalView):
    animal = 'dog'
    sound = 'guau'

class CreateAnimalFormView(View):
    form_class = CreateAnimalForm
    initial = {'name': 'Bobby'}
    template_name = 'class_basics/create_animal.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form['name'].value()
            species = form['species'].value()
            form.save()
            messages.success(request, f'{name} the {species} was created.')
            return redirect('class_basics:success')

        return render(request, self.template_name, {'form': form})
    
########################

class PublisherListView(generic.ListView):
    model = Publisher
    template_name = 'publishers/publishers.html'

    def get_queryset(self):
        return Publisher.objects.all()
    
class PublisherView(generic.DetailView):
    model = Publisher
    template_name = "publishers/publisher.html"
    context_object_name = "publisher"