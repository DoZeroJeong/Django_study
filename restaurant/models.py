from django.db import models

# Create your models here.


class Restaurant_Data(models.Model):
    ddoock = models.CharField(max_length=1024)
    il = models.CharField(max_length=1024)
    rice = models.CharField(max_length=1024)
    noodle = models.CharField(max_length=1024)
    yang = models.CharField(max_length=1024)
    faculty_menu = models.CharField(max_length=1024)
