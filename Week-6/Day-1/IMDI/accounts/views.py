from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# from FilmProject.settings import AUTH_USER_MODEL

# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(LoginRequiredMixin, DetailView): # LoginRequiredMixin - to access users that already login, DetailView - we need to see only about 1 user
    model = User #python bull-in model
    template_name = 'profile.html'
    context_object_name = 'user' # take object to template

    def get_object(self, queryset=None): # take loggedin user
        pk = self.kwargs.get('pk') # take user by id
        return self.request.user #self.query.set - access to user

















# from django.shortcuts import render
# from django.views import generic
# from django.urls import reverse_lazy
# from .models import Director, Film
# from .forms import AddDirectorForm, AddFilmForm


# # def homepage(request):
# #     films = Film.objects.all()
# #     context = {'films': films}
# #     return render(request, 'homepage.html', context)

# class signup(generic.CreateView):
#     template_name = "signup.html"
#     model = Director
#     form_class = AddDirectorForm
#     success_url = reverse_lazy("homepage")


# class login(generic.CreateView):
#     template_name = "login.html"
#     model = Film
#     form_class = AddFilmForm
#     success_url = reverse_lazy("homepage")

# class logout(generic.UpdateView):
#     template_name = "logout.html"
#     model = Director
#     form_class = AddDirectorForm
#     success_url = reverse_lazy("homepage")

# class profile(generic.UpdateView):
#     template_name = "profile.html"
#     model = Director
#     form_class = AddDirectorForm
#     success_url = reverse_lazy("homepage")