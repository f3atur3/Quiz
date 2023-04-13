from django.contrib import admin
from django.urls import path, re_path
from default.views import *
from account.views import *
from victor.views import question

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('all_quiz', all_quiz),
    path('registry', registry),
    path('enter', entry),
    path('us', about),
    path('quiz', quiz_view),
    path('q', question),
]
