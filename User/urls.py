from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('subscribe/', subscribe, name='subscribe'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('member/', member, name='member')
]