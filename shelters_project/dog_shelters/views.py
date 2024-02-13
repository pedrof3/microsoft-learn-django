from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    return HttpResponse("Abrigos e cães")

def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

class DogDetailView(generic.DeleteView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['shelter', 'name', 'description']
