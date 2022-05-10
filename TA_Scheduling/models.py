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

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class course(models.Model):
    courseName = models.CharField(max_length=20)
    courseInstructor = models.CharField(max_length=50)
    meetingTime = models.TimeField()
    sectionNum = models.IntegerField()
    userID = models.ManyToManyField(MyUser)

    def __str__(self):
        return self.courseName

class discussion(models.Model):
    labNum = models.IntegerField()
    labTA = models.CharField(max_length=50)
    courseID = models.ForeignKey(course, on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return "%s" % (self.labNum)


