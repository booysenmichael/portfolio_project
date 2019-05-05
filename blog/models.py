from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pubdate = models.DateField(null=True)
    body = models.TextField(null=True) 
    image = models.ImageField(upload_to='images/') 
