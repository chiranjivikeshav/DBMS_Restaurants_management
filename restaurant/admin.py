from django.contrib import admin

# Register your models here.
from restaurant.models import Userprofile,Restaurant,Item,Manager,Cart,order_details

admin.site.register(Userprofile)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Manager)
admin.site.register(Cart)
admin.site.register(order_details)