# Generated by Django 4.1.4 on 2023-01-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0024_quiz_private_privatequiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
