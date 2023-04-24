from django.shortcuts import render

# Create your views here.

def create_victor(request):
    return render(request, "Creation.html")
