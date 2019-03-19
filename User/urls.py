﻿from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('subscribe/', subscribe),
    path('<str:user>/', getUser),
]