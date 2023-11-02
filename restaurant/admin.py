from django.contrib import admin

# Register your models here.
from restaurant.models import Userprofile,Restaurant,Item
admin.site.register(Userprofile)
admin.site.register(Restaurant)
admin.site.register(Item)