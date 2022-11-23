from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
