from django.db import models

# Create your models here.


class Restaurant_Data(models.Model):
    student_menu = models.CharField(max_length=1024)
    faculty_menu = models.CharField(max_length=1024)
