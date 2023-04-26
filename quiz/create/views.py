from collections import defaultdict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from default.models import Question, Quiz, QIQ
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.
quest = defaultdict(list)


@never_cache
@login_required(login_url='/login/')
def create_victor(request):
    if request.method == "GET":
        id = request.GET.get("id", None)
        if id is not None and len(quest[request.user.id]) > int(id):
            print("ЧИСЛО "+id)
            quest[request.user.id].pop(int(id))
        context = {
            "quiz_questions": [{"id": id, "text": question.ques} for id, question in enumerate(quest.get(request.user.id, []))],
            "count_question": len(quest.get(request.user.id, []))
        }
        print(quest)
        return render(request, "Creation.html", context)
    else:
        print(request.POST)
        quiz = Quiz(q_count=len(quest[request.user.id]), title=request.POST["text"],
                    description=request.POST["text-2"], user_id=request.user, views=0)
        quiz.save()
        for q in quest[request.user.id]:
            q.save()
            QIQ(question=q, quiz=quiz).save()
        quest[request.user.id].clear()
        return redirect(reverse('home'))


@never_cache
@login_required(login_url='/login/')
def create_question_tf(request):
    if request.method == "GET":
        return render(request, "Создание_вопроса_TF.html", )
    elif request.method == "POST":
        quest[request.user.id] = quest.get(request.user.id, [])
        q = Question(ques=request.POST["text"], answer1="true", answer2="false",
                     type_answer="True/False", right_answer=request.POST["radiobutton"])
        quest[request.user.id].append(q)
        return HttpResponse(status=302)


@never_cache
@login_required(login_url='/login/')
def create_question_4(request):
    if request.method == "GET":
        return render(request, "Создание_вопроса_4_ответа.html", )
    elif request.method == "POST":
        quest[request.user.id] = quest.get(request.user.id, [])
        q = Question(ques=request.POST["text"],
                     answer1=request.POST["text-1"],
                     answer2=request.POST["text-2"],
                     answer3=request.POST["text-3"],
                     answer4=request.POST["text-4"],
                     type_answer="radio",
                     right_answer=request.POST["number"])
        quest[request.user.id].append(q)
        return HttpResponse(status=302)


@never_cache
@login_required(login_url='/login/')
def create_question_open(request):
    if request.method == "GET":
        return render(request, "Создание_вопроса_открытый_ответ.html", )
    elif request.method == "POST":
        quest[request.user.id] = quest.get(request.user.id, [])
        q = Question(ques=request.POST["text"], answer1=request.POST["text-1"],
                     type_answer="Вопрос с открытым ответом", right_answer=request.POST["text-1"])
        quest[request.user.id].append(q)
        return HttpResponse(status=302)
