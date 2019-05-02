from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

class test(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    dob =models.DateField(null=True)
  

