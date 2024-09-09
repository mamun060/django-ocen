from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    # class Meta:
    #     permissions = [
    #         ("view_student", "Can view student"),
    #         ("add_student", "Can add student"),
    #         ("change_student", "Can change student"),
    #         ("delete_student", "Can delete student"),
    #     ]
