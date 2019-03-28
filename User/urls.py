from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('subscribe/', subscribe, name='subscribe'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/login/', user_login, name='user_login'),
    path('member/', member, name='member')
]