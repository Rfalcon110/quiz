# Generated by Django 4.1.4 on 2023-01-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0026_delete_privatequiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booleanques',
            name='answer',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default=True, max_length=200),
        ),
    ]
