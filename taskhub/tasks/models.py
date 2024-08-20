from django.db import models

# Create your models here.

class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    username = models.EmailField(max_length=50)


# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateTimeField()
#     completed = models.BooleanField(default=False)
#     # Add more fields as needed