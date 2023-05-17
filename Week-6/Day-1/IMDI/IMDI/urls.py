from django.contrib import admin
from django.urls import path, include 

# from films.views import homepage, addFilm, addDirector, FilmDeleteView, DirectorDeleteView, sfd, sdd, CommentCreateView, RatingCreateView
from accounts.views import SignUpView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView
# from .settings import AUTH_USER_MODEL


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include ("films.urls")),
    path("", include ("accounts.urls")),
# ]



# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('homepage/',homepage, name='homepage'),
    # path('addfilm/', addFilm.as_view(), name = 'addFilm'),
    # path('adddirector/', addDirector),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('accounts/login', LoginView.as_view(), name = 'login'),
    path('accounts/logout', LogoutView.as_view(), name = 'logout'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    # path('deletefilm/<int:pk>', FilmDeleteView.as_view(), name='deletefilm'),
    # path('films/sfd/', sfd, name='sfd'),
    # path('director/sfd/', sdd, name='sdd'),
    # path('deletedirector/<int:pk>', DirectorDeleteView.as_view(), name='deletedirector'),
    # path('homepage/comment/<int:pk>', CommentCreateView.as_view(template_name = 'homepage.html'), name='comment'),
    # path('homepage/rating/<int:pk>', RatingCreateView.as_view(template_name = 'homepage.html'), name='rating'),
]