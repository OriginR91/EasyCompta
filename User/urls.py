from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('subscribe/', subscribe),
    path('account/', include('django.contrib.auth.urls')),
    path('member/', member)
]