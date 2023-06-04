from django.db import models
from django.contrib.auth.models import User

#Класс описывает структуру отношения БД в которой храняться данные определённых вопросов.

class Question(models.Model):
    
    #Класс для перечисления
    class TypesAnswers(models.TextChoices):
        radio = "radio"
        true_false = "True/False"
        open_answer = "Вопрос с открытым ответом"

    
    ques = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=30) 
    answer2 = models.CharField(max_length=30,blank=True,null=True)
    answer3 = models.CharField(max_length=30,blank=True,null=True)
    answer4 = models.CharField(max_length=30,blank=True,null=True)
    type_answer = models.CharField(
        max_length=30,
        choices=TypesAnswers.choices,
        default=TypesAnswers.radio,
    )
    right_answer = models.CharField(max_length=30)

#Класс описывает структуру отношения БД в которой храняться данные определённых викторин.    

class Quiz(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    q_count = models.IntegerField()
    date_of_create = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    views = models.IntegerField()
    icon = models.ImageField()
    count_of_rating=models.IntegerField()
    rating=models.FloatField()

#Класс описывает структуру отношения БД в которой храняться данные связей вопросов и викторин. 

class QIQ(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    quiz = models.ForeignKey(Quiz, on_delete=models.RESTRICT)

#Класс описывает структуру отношения БД в которой храняться данные истории прохождения пользователем викторин.     

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    result = models.FloatField()
