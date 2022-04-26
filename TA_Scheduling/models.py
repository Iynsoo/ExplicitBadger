from django.db import models

# Create your models here.
class Role(models.TextChoices):
    ad = "Admin"
    ins = "Instructor"
    ta = "TA"

class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    userType = models.CharField(choices=Role.choices, default=Role.ta)
    email = models.CharField(max_length=40)
    fname = models.charField(max_length = 20)
    lname = models.charField(max_length = 20)
