from unicodedata import category
from rest_framework import serializers
from .models import Category, Item, Order, ItemOrder
class CategorySerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    def get_item(self,obj):
        items = [{
            "name" : item_obj.name,
            "category" : obj.name,
            "image_url" : item_obj.image_url,
            "category_id": obj.id
        }for item_obj in obj.item_set.all()]
        return items
    class Meta:
        model = Category
        fields = ["item", "name"]

class ItemSerilizer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = ["name", "category","image_url",]

class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerilizer()
    class Meta:
        model = Order  
        fields = ["delivery_address", "order_date", "item"]

class ItemOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    item = ItemSerilizer()
    class Meta:
        model = ItemOrder
        fields = ["order","item","item_count"]