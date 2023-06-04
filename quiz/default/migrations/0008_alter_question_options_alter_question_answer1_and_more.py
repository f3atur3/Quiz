# Generated by Django 4.1.7 on 2023-06-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0007_quiz_count_of_rating_quiz_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['ques'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(max_length=30, verbose_name='Ответ №1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ответ №2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ответ №3'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer4',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ответ №4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques',
            field=models.CharField(max_length=255, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='right_answer',
            field=models.CharField(max_length=30, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type_answer',
            field=models.CharField(choices=[('radio', 'Radio'), ('True/False', 'True False'), ('Вопрос с открытым ответом', 'Open Answer')], default='radio', max_length=30, verbose_name='Тип ответа'),
        ),
    ]
