from django.urls import path, include
from .views import *

urlpatterns = [
    path('regestration', index, name='reg'),
]
