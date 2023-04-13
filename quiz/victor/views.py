from django.shortcuts import get_object_or_404, render
from default.models import Question,Quiz,QIQ
from django.core.paginator import Paginator
from collections import defaultdict

dictan=defaultdict(dict)


def question(request):

    id=request.GET.get('id')
    post=QIQ.objects.filter(quiz=id)
    questions=[post[i].question for i in range(len(post))]
    picture=get_object_or_404(Quiz,id=id)
    per_page = 1
    paginator = Paginator(questions, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    if request.method=='POST':
        dictan[request.user.id].update({page_number:request.POST['radiobutton']})
        print(dictan)
    context={ 'quiz':{
        'id':picture.id,
        'question': {'picture': picture.icon,
                    'num': int(page_number),
                    'question_count': picture.q_count,
                    'text': page_obj[0].ques,
                    'answr': [page_obj[0].answer1,page_obj[0].answer2,page_obj[0].answer3,page_obj[0].answer4],
                    'type':page_obj[0].type_answer,
                    'last_anser':int(dictan[request.user.id].get(page_number,1))
                    } }
    }


    return render(request, "Вопрос.html",context=context)
