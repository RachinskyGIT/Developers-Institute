from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Director, Film
from .forms import AddDirectorForm, AddFilmForm


def homepage(request):
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'homepage.html', context)

class add_director(generic.CreateView):
    template_name = "add_director.html"
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy("homepage")


class add_film(generic.CreateView):
    template_name = "add_film.html"
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy("homepage")

class Edit_Director_View(generic.UpdateView):
    template_name = "edit_director.html"
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy("homepage")

class Edit_Film_View(generic.UpdateView):
    template_name = "edit_film.html"
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy("homepage")