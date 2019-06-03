from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    startdate = models.CharField(max_length=50,null=True)
    returndate = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50) 
    cartype = models.CharField(max_length=50)
    body = models.TextField()
   
    pub_date = models.DateTimeField('date published')