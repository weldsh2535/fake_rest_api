from django.db import models

# Create your models here.
class Students(models.Model):
    StudentId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField()
