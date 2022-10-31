from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group

from .forms import  NewUserForm
from sonips_student.models import Student
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            username = form.cleaned_data.get('username') 

            messages.success(request, "Registration successful." )
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
             
    else:
        form =  NewUserForm()


@unauthenticated_user
def signin( request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'account/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/signin.html', {'form': form})


def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('/')