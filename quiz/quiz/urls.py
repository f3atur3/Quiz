from django.contrib import admin
from django.urls import path
from default.views import *
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('all_quiz', all_quiz),
    path('registry', registration_view),
    path('enter', entry),
    path('us', about),
]