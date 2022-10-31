from django.shortcuts import render
from sonips_student.models import Student

def index(request):

    total = Student.objects.all().count()

    context = { "total":total }
    
    return render(request, 'index.html', context)