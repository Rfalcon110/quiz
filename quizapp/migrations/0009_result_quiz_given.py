# Generated by Django 4.1.4 on 2023-01-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0008_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='quiz_given',
            field=models.BooleanField(default=False),
        ),
    ]
