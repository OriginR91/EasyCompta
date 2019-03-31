from django.urls import path
from Accounting.views import *

urlpatterns = [
    path('', home, name='home'),
    path('devis/', devis, name='devis'),
    path('facture/', facture, name='facture')
]