# Generated by Django 4.1.7 on 2023-04-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_quiz_description_quiz_q_count_quiz_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=15),
        ),
    ]
