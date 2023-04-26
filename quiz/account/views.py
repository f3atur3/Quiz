from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from victor.views import dictan
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from default.models import *

#Класс обработчика выхода из системы
class CustomLogoutView(LogoutView):
    next_page = '/'
    #Удаление сессионных данных для пользователя
    def dispatch(self, request, *args, **kwargs):
        dictan.pop(request.user.id, None)
        return super().dispatch(request, *args, **kwargs)

#Класс обработчика входа в систему
class CustomLoginView(LoginView):

    template_name = 'registration/login.html'

    #Праверка корректности данных в форме 
    def form_valid(self, form):
        return super().form_valid(form)
    
    #Отправка url
    def get_success_url(self):
        return self.request.GET.get('next', '/')
 

#Обработчик регистрации пользователя
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'Регистрация.html', {'form': form})

#Обработчик Персональной страницы пользователя
@login_required(login_url='/login/')
def personal_account(request):
    quizes = History.objects.filter(user=request.user)
    context = {
        'user': {
            'picture': 'pinguin.png',
            'cnt_complited_quiz': len(quizes.distinct()),
            'perсent_crrct_answ': round(sum([q.result * 100 for q in quizes]) / max(1, len(quizes)),2)
        }
    }
    return render(request, 'Кабинет.html', context=context)

#Обработчик Персональной страницы пользователя
@login_required(login_url='/login/')
def personal_history(request):
    quizes = History.objects.filter(user=request.user.id).order_by('-date')
    per_page = 10
    paginator = Paginator(quizes, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'complited_quiz' : [
            {
                'title': page_obj[i].quiz.title,
                'date': page_obj[i].date,
                'result': round(page_obj[i].result*100,2),
                'count_page': int(paginator.num_pages),
                'page': int(page_number)
            } for i in range(len(page_obj))
        ]
    }
    return render(request, 'История.html', context=context)