from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {
        'form': form
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {
        'form': form
    })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def profile(request):
    return render(request, 'profile.html')
