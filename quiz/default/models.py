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
    title = models.CharField(max_length=20, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")
    q_count = models.IntegerField(verbose_name="Кол-во вопросов")
    date_of_create = models.DateField(auto_now=True, verbose_name="Дата создания")
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Создатель")
    views = models.IntegerField(verbose_name="Кол-во просмотров")
    icon = models.ImageField(verbose_name="Картинка")
    count_of_rating=models.IntegerField(verbose_name="Кол-во оценок")
    rating=models.FloatField(verbose_name="Рейтинг", db_index=True)
    
    class Meta :
        verbose_name_plural = 'Викторины'
        verbose_name = 'Викторина'
        ordering = ['-rating']
    
    def __str__(self):
        return self.title

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
