from django.db import models

# Create your models here.
class Teacher(models.Model):
    firstname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)