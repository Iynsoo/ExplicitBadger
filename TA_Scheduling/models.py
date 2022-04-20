from django.db import models

# Create your models here.

class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)