from django.shortcuts import render

def entry(request):
    return render(request, "Вход.html")

def registry(request):
    return render(request, "Регистрация.html")