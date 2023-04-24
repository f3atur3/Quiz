from urllib.parse import urlencode
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from default.models import Quiz, QIQ, History
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from collections import defaultdict
from django.contrib.auth.decorators import login_required

#Словарь для хранения выбранных пользователем вариантов ответа
dictan=defaultdict(dict)

@login_required(login_url='/login/')
def results(request):
    id = request.GET.get('id')
    if request.method == 'POST':
        current_quiz = Quiz.objects.get(id=id)
        current_quiz.views += 1
        current_quiz.save()
    post = QIQ.objects.filter(quiz=id).order_by('question')
    questions = [post[i].question for i in range(len(post))]
    # results_ = [str(i.right_answer) == str(j) for i, j in zip(questions, dictan[request.user.id][id])]
    results_ = list()
    for i, q in enumerate(questions):
        ans = dictan[request.user.id][id].get(i+1, None)
        results_.append(int(ans is not None))
    dictan[request.user.id].pop(id, None)
    context = {
        'correct_answ': sum(results_),
        'all_answ': len(results_)
    }
    History.objects.create(
        user=User.objects.get(id=request.user.id),
        quiz=Quiz.objects.get(id=id),
        result=context['correct_answ']/context['all_answ']
    )
    return render(request, "Результат.html",context=context)

#Функция создаёт контекст и генерирует шаблон динамической страницы Вопрос
@login_required(login_url='/login/')
def question(request):
    id = request.GET.get('id')
    post = QIQ.objects.filter(quiz=id).order_by('question')
    questions = [post[i].question for i in range(len(post))]
    picture = get_object_or_404(Quiz,id=id)
    per_page = 1
    paginator = Paginator(questions, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        dictan[request.user.id][id] = dictan[request.user.id].get(id,{}) 
        dictan[request.user.id][id].update({page_number:request.POST['radiobutton']})
        print(page_number, paginator.num_pages)
        if int(page_number) == int(paginator.num_pages):
            print('redirect')
            return redirect('{}?{}'.format(reverse(results), urlencode({'id':id})))
        elif int(page_number) < int(paginator.num_pages):
            return redirect('{}?{}'.format(reverse(question), urlencode({'id':id,'page':int(page_number)+1})))
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
