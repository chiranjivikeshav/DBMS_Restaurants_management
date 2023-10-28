from django.db import models
from django.contrib.auth.models import User
import datetime

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    user_about = models.TextField()
    contact_number = models.CharField(max_length=15)
    user_email = models.EmailField()
    user_address = models.CharField(max_length=200)
    user_city = models.CharField(max_length=100)
    user_country = models.CharField(max_length=100)
    user_state = models.CharField(max_length=100,null=True)
    user_ZIPCODE = models.IntegerField(null=True)
    def __str__(self):
        return self.user_name
