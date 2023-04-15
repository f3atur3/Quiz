from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from victor.views import dictan
from django.contrib.auth.decorators import login_required
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
            'perсent_crrct_answ': sum([q.result * 100 for q in quizes]) / max(1, len(quizes))
        }
    }
    return render(request, 'Кабинет.html', context=context)

#Обработчик Персональной страницы пользователя
@login_required(login_url='/login/')
def personal_history(request):
    quizes = History.objects.filter(user=request.user)
    context = {
        'complited_quiz' : [
            {
                'title': quizes[i].quiz.title,
                'date': quizes[i].date,
                'result': quizes[i].result
            } for i in range(len(quizes))
        ]
    }
    return render(request, 'История.html', context=context)