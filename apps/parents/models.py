from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.students.models import Student


class Parent(models.Model):
    STATUS = [("active", "Active"), ("inactive", "Inactive")]

    GENDER = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(max_length=10, choices=STATUS, default="active")
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    child = models.ForeignKey(Student, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")  

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )
    alternative_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name}"

    def get_absolute_url(self):
        return reverse("parent-detail", kwargs={"pk": self.pk})