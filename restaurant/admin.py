from django.contrib import admin

# Register your models here.
from restaurant.models import Userprofile,Restaurant,Item,Manager,Cart,Order,OrderItem,Feedback,PaymentHistory
admin.site.register(Userprofile)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Manager)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Feedback)
admin.site.register(PaymentHistory)