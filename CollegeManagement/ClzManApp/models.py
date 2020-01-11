from django.db import models


# Create your models here.
class Students(models.Model):
    StudentID=models.CharField(max_length=255)
    StudentName=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    standard=models.CharField(max_length=255)

    def __str__(self):
        return  str(self.id) + " " + self.StudentID + " " + self.StudentName + " " + self.email + " " + self.standard


class Teachers(models.Model):
    TeacherID=models.CharField(max_length=255)
    TeacherName=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    department=models.CharField(max_length=255)

    def __str__(self):
        return  str(self.id) + " " + self.TeacherID + " " + self.TeacherName + " " + self.email + " " + self.department
