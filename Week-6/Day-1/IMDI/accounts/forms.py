from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# class CustomSignUpForm(UserCreationForm):

#     class Meta (UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + ("film_reviewed",)



class UserProfileForm(UserChangeForm):

    class Meta:
        model = Profile
        exclude = ['user']



# class LoginForm(forms.Form):

#     Username = forms.CharField()
#     Password = forms.PasswordInput()





# class SignupForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
