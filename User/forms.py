from django import forms
from User.models import User

class UserForm(forms.ModelForm) :
    emailConfirm = forms.EmailField(max_length=70, label='Confirmez l\'email')
    passwordConfirm = forms.CharField(max_length=30, label='Confirmez le mot de passe')

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
        fields = (
            'nom', 
            'prenom', 
            'email',
            'emailConfirm',
            'societe', 
            'adresse', 
            'cp', 
            'ville', 
            'pathlogo', 
            'pseudo', 
            'password',
            'passwordConfirm'
        )
