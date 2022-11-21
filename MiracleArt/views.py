from django.shortcuts import render

from .models import Pin, PinCategory


def index(request):
    return render(request, 'index.html')


def gallery(request, category_id=None):
    context = {
        'pins': Pin.objects.all(),
        'categories': PinCategory.objects.all(),
    }
    if category_id:
        context.update({'pins': Pin.objects.filter(category_id=category_id)})
    else:
        context.update({'pins': Pin.objects.all()})
    return render(request, 'gallery.html', context)


def images(request):
    return render(request, 'images.html')
