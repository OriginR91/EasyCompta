from django import forms
from Client.models import Client

class ClientForm(forms.ModelForm) :
    class Meta:
        model = Client
        fields = (
            'client_nom',
            'client_siret',
            'client_adresse',
            'client_cp',
            'client_ville'
        )