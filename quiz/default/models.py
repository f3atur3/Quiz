from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    
    #Класс для перечисления
    class TypesAnswers(models.TextChoices):
        radio = "radio"
        true_false = "True/False"
        open_answer = "Вопрос с открытым ответом"

    
    ques = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=30)
    answer2 = models.CharField(max_length=30)
    answer3 = models.CharField(max_length=30)
    answer4 = models.CharField(max_length=30)
    type_answer = models.CharField(
        max_length=30,
        choices=TypesAnswers.choices,
        default=TypesAnswers.radio,
    )
    right_answer = models.CharField(max_length=30)
    
class Quiz(models.Model):
    date_of_create = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    views = models.IntegerField()
    rating = models.FloatField()
    icon = models.ImageField()

class QIQ(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    quiz = models.ForeignKey(Quiz, on_delete=models.RESTRICT)
    