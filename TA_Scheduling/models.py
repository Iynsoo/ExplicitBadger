from django.db import models

# Create your models here.
class Role(models.TextChoices):
    ad = "Admin"
    ins = "Instructor"
    ta = "TA"

class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    userType = models.CharField(max_length=10, choices=Role.choices, default=Role.ta)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
