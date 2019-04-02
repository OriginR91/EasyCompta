from django.urls import path
from Client.views import *

urlpatterns = [
    path('', home, name='homeClient')
]