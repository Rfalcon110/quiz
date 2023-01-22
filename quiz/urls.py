"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from quizapp import views as quiz_views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('quiz/',include('quizapp.urls')),
   path('register/',user_views.register,name= 'register'),
   path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
   path('logout/', user_views.logoutPage,name='logout'),
   path('',user_views.home,name='home'),
   path('addquestion/',quiz_views.addQuestion,name='addquestion'),
   path('addquiz/',quiz_views.addquiz,name='addquiz'),
   path('registeradmin/',user_views.register_as_admin,name= 'registerqm'),
   path('edit/',quiz_views.edit_index,name='editindex'),
   path('edit/<str:quiz_name1>/',quiz_views.edit_quiz,name='editquiz'),
   path('edit/<str:quiz_name1>/<str:id>/',quiz_views.editquestion,name='editquestion'),
   path("", include("allauth.urls")),
   path('leaderboards/',quiz_views.leaderboards_index,name='leaderboardsindex'),
   path('leaderboards/<str:quiz_name1>/',quiz_views.leaderboards,name='leaderboards'),
   path('privatequiz/',quiz_views.private_quiz_index,name='private_quiz_index'),
   path('privatequiz/<str:quiz_name1>/',quiz_views.leaderboards,name='privatequiz'),
]
