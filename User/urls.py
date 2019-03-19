from django.urls import path
from User.views import *

urlpatterns = [
    path('', index),
    path('subscribe/', subscribe),
    path('<str:user>/', getUser),
]