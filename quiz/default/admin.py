from django.contrib import admin
from default.models import *

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass

@admin.register(QIQ)
class QIQAdmin(admin.ModelAdmin):
    pass