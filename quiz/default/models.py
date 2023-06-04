from django.db import models
from django.contrib.auth.models import User

#Класс описывает структуру отношения БД в которой храняться данные определённых вопросов.

class Question(models.Model):
    
    #Класс для перечисления
    class TypesAnswers(models.TextChoices):
        radio = "radio"
        true_false = "True/False"
        open_answer = "Вопрос с открытым ответом"

    
    ques = models.CharField(max_length=255, verbose_name="Вопрос")
    answer1 = models.CharField(max_length=30, verbose_name="Ответ №1") 
    answer2 = models.CharField(max_length=30,blank=True,null=True, verbose_name="Ответ №2")
    answer3 = models.CharField(max_length=30,blank=True,null=True, verbose_name="Ответ №3")
    answer4 = models.CharField(max_length=30,blank=True,null=True, verbose_name="Ответ №4")
    type_answer = models.CharField(
        max_length=30,
        choices=TypesAnswers.choices,
        default=TypesAnswers.radio,
        verbose_name="Тип ответа"
    )
    right_answer = models.CharField(max_length=30, verbose_name="Правильный ответ")
    
    class Meta :
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
    
    def __str__(self):
        return self.ques

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
    question = models.ForeignKey(Question, on_delete=models.RESTRICT, verbose_name="Вопрос")
    quiz = models.ForeignKey(Quiz, on_delete=models.RESTRICT, verbose_name="Викторина")
    
    class Meta :
        verbose_name_plural = 'Вопросы в викторинах'
        verbose_name = 'Вопросы в викторинах'

#Класс описывает структуру отношения БД в которой храняться данные истории прохождения пользователем викторин.     

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    result = models.FloatField()
