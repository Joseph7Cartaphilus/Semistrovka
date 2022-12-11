from django.shortcuts import render, get_object_or_404, redirect

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


def workshop(request):
    pins = Pin.objects.all()
    return render(request, 'workshop.html', {
        'pins': pins
    })


def show_one_pin_by_slug_id(request, slug_pin: str, id: int):
    pin = get_object_or_404(Pin, slug=slug_pin, id=id)
    return render(request, 'one_pin.html', {
        'pin': pin,
        'id': pin.id,
        'slug': pin.slug
    })


def delete_pin(request, slug_pin: str):
    Pin.objects.get(slug=slug_pin).delete()
    return redirect('workshop')
