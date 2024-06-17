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
    user_ZIPCODE = models.IntegerField(default=000000)
    def __str__(self):
        return self.user_name

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True)
    rest_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)  
    pin = models.IntegerField() 
    state = models.CharField(max_length=100)
    rest_cantact_no = models.IntegerField()
    owner_contact_no = models.IntegerField()  
    ownername= models.CharField(max_length=100)  
    owneremail = models.EmailField(max_length=100)  
    open_time = models.TimeField()  
    close_time = models.TimeField()  
    menu_image = models.ImageField(upload_to='menu_images/')
    restaurant_image = models.ImageField(upload_to='resta_images/')
    def __str__(self):
        return self.rest_name

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/',null=True)
    item_rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    people_rated = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.item_name

class Manager(models.Model):
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE)
    Name = models.TextField()
    Contact = models.TextField()
    Email = models.TextField()
    Address = models.TextField()
    BankName = models.TextField()
    BankBranch = models.TextField()
    BankIFSC = models.TextField()
    BankAccount = models.TextField()
    About = models.TextField()
    def __str__(self):
        return self.restaurant.rest_name
class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_count = models.IntegerField(default=1)
    def __str__(self):
        return self.item.item_name
class order_details(models.Model):
    Name = models.TextField()
    phone_number = models.IntegerField()
    Email = models.TextField()
    Address = models.TextField()
    city=models.TextField()
    state=models.TextField()
    pin_code=models.IntegerField()
    orders=models.ForeignKey(Item, on_delete=models.CASCADE)
    payment_status=models.BooleanField(default=False)
    def __str__(self):
        return self.Name
    




