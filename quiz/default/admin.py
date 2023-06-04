from django.contrib import admin
from default.models import *

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ques', 'right_answer')
    list_display_links = ('id', 'ques', 'right_answer')
    search_fields = ('id', 'ques', 'right_answer')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'q_count', 'date_of_create', 'user_id', 'views', 'rating')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')

@admin.register(QIQ)
class QIQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'quiz')
    list_display_links = ('id', 'question', 'quiz')
    search_fields = ('id', 'question', 'quiz')