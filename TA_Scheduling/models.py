from django.db import models

# Create your models here.
class Role(models.TextChoices):
    admin = "Admin"
    instructor = "Instructor"
    ta = "TA"

class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    userType = models.CharField(max_length=10, choices=Role.choices, default=Role.ta)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class course(models.Model):
    courseName = models.CharField(max_length=20)
    courseInstructor = models.CharField(max_length=20)
    meetingTime = models.TimeField()
    sectionNum = models.IntegerField()

class discussion(models.Model):
    labNum = models.IntegerField()
    labTA = models.CharField(max_length= 20)


