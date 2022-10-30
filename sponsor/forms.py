from socket import fromshare
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Sponsor,Athlete


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class SponsorForm(ModelForm):
    
    name= forms.TextInput()
    email= forms.EmailInput()
    image= forms.ImageField()
    offer= forms.TextInput()
    class Meta:
        model = Sponsor
        fields="__all__"

class AthleteForm(ModelForm):
    f_name= forms.TextInput()
    l_name= forms.TextInput()
    email= forms.EmailInput()
    image= forms.ImageField()
    sport= forms.TextInput()
    description= forms.TextInput()


    class Meta:
        model = Athlete
        fields="__all__"
