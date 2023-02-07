from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    quiz_name=models.CharField(max_length=200,)
    private=models.BooleanField(default=False)
    password=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.quiz_name


class Scq(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    question_text=models.CharField(max_length=200,null=True,blank=True)
    choice_1=models.CharField(max_length=200,null=True,blank=True)
    choice_2=models.CharField(max_length=200,null=True,blank=True)
    choice_3=models.CharField(max_length=200,null=True,blank=True)
    choice_4=models.CharField(max_length=200,null=True,blank=True)
    answer=models.CharField(max_length=200,null=True,blank=True)
    question_type='SCQ'
    marking_scheme=[
        ('nonegmarking','+4/0'),
        ('negmarking','+4/-1')
    ]
    marking=models.CharField(max_length=200,choices=marking_scheme, default='nonnegmarking')
    def  __str__(self):
        return self.question_text
    def question_type(self):
        return self.question_type

class intques(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    question_text=models.CharField(max_length=200,null=True,blank=True)
    answer=models.IntegerField()
    question_type='integer'
    marking_scheme=[
        ('nonegmarking','+4/0'),
        ('negmarking','+4/-1')
    ]
    marking=models.CharField(max_length=200,choices=marking_scheme, default='nonnegmarking')
    def __str__(self):
        return self.question_text
    def question_type(self):
        return self.question_type


class booleanques(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    question_text=models.CharField(max_length=200,null=True,blank=True)
    choice=[
        ('true','True'),
        ('false','False')
    ]
    answer=models.CharField(max_length=200,choices=choice,default=True)
    question_type='boolean'
    marking_scheme=[
        ('nonegmarking','+4/0'),
        ('negmarking','+4/-1')
    ]
    marking=models.CharField(max_length=200,choices=marking_scheme, default='nonnegmarking')
    def __str__(self):
        return self.question_text
    def question_type(self):
        return self.question_type
    
class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    correct=models.IntegerField(default=0)
    wrong=models.IntegerField(default=0) 
    marks_scored=models.IntegerField(default=0) 
    maximum_marks=models.IntegerField(default=0)
    quiz_given=models.BooleanField(default=False)  
    
class Mcq(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    
    question_text=models.CharField(max_length=200,null=True,blank=True)
    choice=[
        ('true','True'),
        ('false','False')
    ]
    choice_1=models.CharField(max_length=200,null=True,blank=True)
    choice_1_ans=models.CharField(max_length=200,choices=choice,null=True,blank=True)
    choice_2=models.CharField(max_length=200,null=True,blank=True)
    choice_2_ans=models.CharField(max_length=200,choices=choice,null=True,blank=True)
    choice_3=models.CharField(max_length=200,null=True,blank=True)
    choice_3_ans=models.CharField(max_length=200,choices=choice,null=True,blank=True)
    choice_4=models.CharField(max_length=200,null=True,blank=True)
    choice_4_ans=models.CharField(max_length=200,choices=choice,null=True,blank=True)
    
    question_type='MCQ'
    marking_scheme=[
        ('nonegmarking','+4/0'),
        ('negmarking','+4/-1')
    ]
    marking=models.CharField(max_length=200,choices=marking_scheme, default='nonnegmarking')
    def  __str__(self):
        return self.question_text
    def question_type(self):
        return self.question_type