from django import forms
from django.contrib.auth.models import User
from User.models import Profil

class UserForm(forms.ModelForm) :
    emailConfirm = forms.EmailField(max_length=70, label='Confirmez l\'email')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    passwordConfirm = forms.CharField(max_length=30, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'passwordConfirm',
            'email',
            'emailConfirm',
            'last_name',
            'first_name'
        )
        

class ProfilForm(forms.ModelForm) :
    class Meta:
        model = Profil
        labels = {
            'societe': 'Société',
            'cp': 'Code postal',
            'pathlogo': 'Logo'
        }
        fields = (
            'societe',
            'adresse',
            'cp',
            'ville',
            'pathlogo'
        )