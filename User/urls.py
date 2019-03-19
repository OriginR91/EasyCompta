from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('subscribe/', subscribe),
    path('subscribe/error/', subscribe),
    path('<str:user>/', getUser),
]