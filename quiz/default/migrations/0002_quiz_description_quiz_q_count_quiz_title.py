# Generated by Django 4.1.7 on 2023-04-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='Описание', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='q_count',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='Title', max_length=30),
            preserve_default=False,
        ),
    ]
