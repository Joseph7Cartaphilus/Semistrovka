from django.shortcuts import render

from .models import Pin


def index(request):
    return render(request, 'index.html')


def gallery(request):
    context = {
        'pins': Pin.objects.all(),
    }
    return render(request, 'gallery.html', context)
