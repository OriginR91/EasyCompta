from django.urls import path
from Client.views import *

urlpatterns = [
    path('', homeClient, name='homeClient'),
    path('addClient/', addClient, name='addClient'),
    path('detailClient/<int:pk>/', detailClient, name='detailClient'),
    path('manageClient/', manageClient, name='manageClient')
]