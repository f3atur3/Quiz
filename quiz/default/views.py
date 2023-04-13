from django.shortcuts import get_object_or_404, render

from default.models import Quiz

def index(request):
    posts = Quiz.objects.all().order_by('-rating')
    posts=posts[:4]
    context={
        'quiz':[
                {
                'picture': posts[0].icon,
                'rating': posts[0].rating,
                'id': posts[0].id,
                },
                {
                'picture': posts[1].icon,
                'rating': posts[1].rating,
                'id': posts[1].id,
                },
                {
                'picture': posts[2].icon,
                'rating': posts[2].rating,
                'id': posts[2].id,
                },
                {
                'picture': posts[3].icon,
                'rating': posts[3].rating,
                'id': posts[3].id,
                }
        ]
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
        }
    }
    return render(request, "Просмотр.html",context=context)

