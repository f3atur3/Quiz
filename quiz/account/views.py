from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm

def entry(request):
    return render(request, "Вход.html")

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # redirect to the homepage on successful registration
    else:
        form = RegistrationForm()
    return render(request, 'Регистрация.html', {'form': form})