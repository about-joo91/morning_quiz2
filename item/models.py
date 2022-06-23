from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)   # food, appliance clothes

    class Meta:
        db_table = "categories"

class Item(models.Model):
    name = models.CharField(max_length=100)    # food : pizza, hamburger // appliance : air conditioner, dryer
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image_url = models.URLField()

    class Meta:
        db_table = 'items'


class Order(models.Model):
    delivery_address = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    item = models.ManyToManyField('Item', through='ItemOrder')

    class Meta:
        db_table = 'orders'

class ItemOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    item_count = models.IntegerField()

    class Meta:
        db_table = 'item_orders'
