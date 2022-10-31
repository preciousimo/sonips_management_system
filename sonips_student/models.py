from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    mother_name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    religion = models.CharField(max_length=200, null=True)
    klass = models.CharField(max_length=200, null=True)
    image = models.ImageField(default="figure/admin.png", null=True, blank=True)
    admission_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user.username