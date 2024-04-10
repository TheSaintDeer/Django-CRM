from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    channels = Channel.objects.all()

    return render(request, 'core/index.html', {'channels': channels})