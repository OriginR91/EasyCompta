from django import forms
from User.models import User

class UserForm(forms.ModelForm) :
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'prenom': 'Prénom',
            'societe': 'Société',
            'cp': 'Code postal',
            'pathlogo': 'Logo',
            'password': 'Mot de passe'
        }
        fields = ('nom', 'prenom', 'societe', 'adresse', 'cp', 'ville', 'pathlogo', 'pseudo', 'password')
        