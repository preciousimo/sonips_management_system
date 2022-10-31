from django.shortcuts import render

def profile(request):

    context = {}
    
    return render(request, 'base/profile.html', context)