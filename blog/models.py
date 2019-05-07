from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pubdate = models.DateField(null=True)
    body = models.TextField(null=True) 
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]

    def pub_date_pretty(self):
        return self.pubdate.strftime('%Y-%m-%d')
