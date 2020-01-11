from django.db import models

# Create your models here.
class Students(models.Model):
    StudentID=models.CharField(max_length=50)
    StudentName=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    standard=models.CharField(max_length=255)

    def __str__(self):
        return self.StudentName


class Teachers(models.Model):
    TeacherID=models.CharField(max_length=50)
    TeacherName=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    department=models.CharField(max_length=255)

    def __str__(self):
        return self.TeacherName