from django.contrib import admin
from django.urls import path
from default.views import *
from account.views import *
from victor.views import *

#Сопоставление ссылкам их обработчиков
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('all_quiz', all_quiz),
    path('registry', registration_view),
    path('us', about),
    path('quiz', quiz_view),
    path('q', question),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('cabinet', personal_account),
    path('history', personal_history),
    path('result', results, name='res')
]
