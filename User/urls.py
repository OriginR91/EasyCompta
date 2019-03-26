from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('subscribe/', subscribe, name='subscribe'),
    path('account/', include('django.contrib.auth.urls')),
    path('member/', member, name='member')
]