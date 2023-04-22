from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Family, Animal

class AnimalsInFamilyView(ListView):
    model = Animal
    template_name = 'animals_in_family.html'
    context_object_name = 'animals'

    def get_queryset(self):
        return Animal.objects.filter(family_id=self.kwargs['pk'])

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal_detail.html'