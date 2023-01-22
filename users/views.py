from django.shortcuts import render,redirect
from .forms import UserCreationForm
from django.contrib.auth.models import User,Permission
from django.contrib.auth import login,logout
from django.contrib.contenttypes.models import ContentType
from quizapp.models import Quiz,Scq


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register') 
    else:
        form=UserCreationForm()
        return render(request,'users/register.html',{'form':form})   


def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')
 

def logoutPage(request):
    logout(request)
    return redirect('/')

def register_as_admin(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(username,password=password)
            content_type = ContentType.objects.get_for_model(Quiz)
            post_permission = Permission.objects.filter(content_type=content_type)
            for perm in post_permission:
                user.user_permissions.add(perm)
            content_type = ContentType.objects.get_for_model(Scq)
            post_permission = Permission.objects.filter(content_type=content_type)
            for perm in post_permission:
                user.user_permissions.add(perm)
            user.save()
            login(request,user)
            return redirect('login')
        else:
            return redirect('register') 
    else:
        form=UserCreationForm()
        return render(request,'users/register.html',{'form':form})
    