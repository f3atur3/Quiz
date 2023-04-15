from django.shortcuts import get_object_or_404, render
from default.models import Quiz, QIQ
from django.core.paginator import Paginator
from collections import defaultdict
from django.contrib.auth.decorators import login_required

#Словарь для хранения выбранных пользователем вариантов ответа
dictan=defaultdict(dict)

#Функция создаёт контекст и генерирует шаблон динамической страницы Вопрос
@login_required(login_url='/login/')
def question(request):
    id = request.GET.get('id')
    post = QIQ.objects.filter(quiz=id)
    questions = [post[i].question for i in range(len(post))]
    picture = get_object_or_404(Quiz,id=id)
    per_page = 1
    paginator = Paginator(questions, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        dictan[request.user.id][id] = dictan[request.user.id].get(id,{}) 
        dictan[request.user.id][id].update({page_number:request.POST['radiobutton']})   
    try:
       last_anser=dictan[request.user.id][id].get(page_number,1)
    except:
        last_anser=1
    context={ 'quiz':{
        'id':picture.id,
        'question': {'picture': picture.icon,
                    'num': int(page_number),
                    'question_count': picture.q_count,
                    'text': page_obj[0].ques,
                    'answr': [page_obj[0].answer1,page_obj[0].answer2,page_obj[0].answer3,page_obj[0].answer4],
                    'type':page_obj[0].type_answer,
                    'last_anser':int(last_anser)
                    } }
    }


    return render(request, "Вопрос.html",context=context)
