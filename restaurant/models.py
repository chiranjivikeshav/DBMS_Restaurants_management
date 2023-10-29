from django.db import models

# Create your models here.



   
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)  
    pin = models.IntegerField(max_length=10) 
    state = models.CharField(max_length=100)
    no = models.IntegerField(max_length=20)
    ownerno = models.IntegerField(max_length=20)  
    ownername= models.CharField(max_length=100)  
    owneremail = models.EmailField(max_length=100)  
    open_time = models.TimeField()  
    close_time = models.TimeField()  
