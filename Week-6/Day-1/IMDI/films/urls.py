from django.urls import path
from . import views
from .views import add_director, add_film, Edit_Director_View, Edit_Film_View

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('add_director/', add_director.as_view(), name='add_director'),
    path('add_film/', add_film.as_view(), name='add_film'),
    path('edit_director/<int:pk>/', Edit_Director_View.as_view(), name='edit_director'),
    path('edit_film/<int:pk>/', Edit_Film_View.as_view(), name='edit_film'),
]
