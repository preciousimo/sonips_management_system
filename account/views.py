from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def signin(request):
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