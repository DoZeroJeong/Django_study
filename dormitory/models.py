from django.db import models

# Create your models here.


class Tu_Data(models.Model):
    tu_id = models.CharField(max_length=50)
    tu_password = models.CharField(max_length=50)
    first_day = models.CharField(max_length=10)
    second_day = models.CharField(max_length=10)
    apply_text = models.TextField()