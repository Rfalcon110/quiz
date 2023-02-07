from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<str:quiz_name1>/',views.quiz, name='quiz'),
   
]