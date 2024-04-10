from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('registration/', include('registration.urls')),
    path('chat/', include('chat.urls'))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
