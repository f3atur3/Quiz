from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
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
    search = request.GET.get('search')
    if search is None:
        object_list = Quiz.objects.all()
    else:
        object_list = Quiz.objects.filter(title__icontains=search)
    per_page = 10
    paginator = Paginator(object_list, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'quizzes': [ {
            'picture': page_obj[i].icon,
            'rating': page_obj[i].rating,
            'id': page_obj[i].id,
            "description": page_obj[i].description,
            "title": page_obj[i].title,
            "num_complition": page_obj[i].views
            } for i in range(len(page_obj))]
    }
    print(context) 
    return render(request, "Все_викторины.html", context=context)


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
            'id':post.id
        }
    }
    return render(request, "Просмотр.html",context=context)

