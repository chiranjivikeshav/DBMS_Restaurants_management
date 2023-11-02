from django.db import models


class Item(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)