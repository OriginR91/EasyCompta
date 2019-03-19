from django import forms
from User.models import User

class UserForm(forms.ModelForm) :
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('nom', 'prenom', 'societe', 'adresse', 'cp', 'ville', 'pathlogo', 'pseudo', 'password')
        