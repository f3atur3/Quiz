from django.shortcuts import get_object_or_404, render
from default.models import Question

def question(request):
    id=request.GET.get('id')
    post = get_object_or_404(Question, id=id)
    context={ 'quiz':{
        'question': {'text':post.ques,
                     'type': post.type_answer,
                     'answr': [post.answer1,post.answer2,post.answer3,post.answer4],
                     } }
    }
    return render(request, "Вопрос.html",context=context)