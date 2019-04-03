from django.urls import path
from Accounting.views import *

urlpatterns = [
    path('', homeAccounting, name='homeAccounting'),
    path('devis/', devis, name='devis'),
    path('facture/', facture, name='facture')
]