# Generated by Django 4.1.4 on 2023-01-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0022_alter_booleanques_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq',
            name='choice_1_ans',
            field=models.CharField(blank=True, choices=[('true', 'True'), ('false', 'False')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_2_ans',
            field=models.CharField(blank=True, choices=[('true', 'True'), ('false', 'False')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_3_ans',
            field=models.CharField(blank=True, choices=[('true', 'True'), ('false', 'False')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_4_ans',
            field=models.CharField(blank=True, choices=[('true', 'True'), ('false', 'False')], max_length=200, null=True),
        ),
    ]