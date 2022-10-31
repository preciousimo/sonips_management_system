from django.shortcuts import render

def index(request):

    context = {}
    
    return render(request, 'index.html', context)

def profile(request):

    context = {}
    
    return render(request, 'profile.html', context)