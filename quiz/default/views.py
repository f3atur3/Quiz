from django.shortcuts import render

def index(request):
    return render(request, "Главная.html")

def all_quiz(request):
    return render(request, "Все_викторины.html")

def quiz(request):
    return render(request, "Просмотр.html")

def about(request):
    return render(request, "Мы.html")

def entry(request):
    return render(request, "Вход.html")

def registry(request):
    return render(request, "Регистрация.html")