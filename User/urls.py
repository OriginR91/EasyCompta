from django.urls import path
from User import views

urlpatterns = [
    path('', views.index),
    path('subscribe/', views.subscribe),
    path('<str:user>/', views.getUser),
]