from django.contrib import admin
from django.urls import path
from default.views import *
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('all_quiz', all_quiz),
    path('registry', registry),
    path('enter', entry),
    path('us', about),
]
