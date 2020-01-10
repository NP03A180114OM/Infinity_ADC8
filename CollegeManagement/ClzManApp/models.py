from django.db import models


# Create your models here.
class Students(models.Model):
    StudentID=models.CharField(max_length=255)
    StudentName=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    standard=models.CharField(max_length=255)
    profile_image=models.FileField()


class Teachers(models.Model):
    TeacherID=models.CharField(max_length=255)
    TeacehrName=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    department=models.CharField(max_length=255)