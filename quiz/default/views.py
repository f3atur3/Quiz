from django.shortcuts import get_object_or_404, render

from default.models import Quiz

def index(request):
    posts = Quiz.objects.all().order_by('-rating')
    posts=posts[:4]
    context = {
        'quiz': [ {
            'picture': posts[i].icon,
            'rating': posts[i].rating,
            'id': posts[i].id,
            "description": posts[i].description,
            "title": posts[i].title,
            } for i in range(4)]
    }
    
    return render(request, "Главная.html",context=context)


def all_quiz(request):
    return render(request, "Все_викторины.html")


def about(request):
    return render(request, "Мы.html")


def quiz(request):
    return render(request, "Просмотр.html")

def quiz_view(request):
    id=request.GET.get('id')
    post = get_object_or_404(Quiz, id=id)
    context={
        'quiz':{
            "picture": post.icon,
            "rating": post.rating,
            "num_complition": post.views,
            "description": post.description,
            "title": post.title,
        }
    }
    return render(request, "Просмотр.html",context=context)

