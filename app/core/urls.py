from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('registration/', include('registration.urls')),
    path('chat/', include('chat.urls'))
]
