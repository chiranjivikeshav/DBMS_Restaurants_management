from django.contrib import admin

# Register your models here.
from django.contrib import admin
from restaurant.models import Item
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=('restaurant','item_name','price')

admin.site.register(Item,useradmin)