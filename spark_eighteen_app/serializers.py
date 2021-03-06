from rest_framework import serializers
from .models import *


class RestaurentSerializer(serializers.ModelSerializer):
    restaurent_schedule = serializers.StringRelatedField(
        many=True, read_only=True)

    restaurent_product = serializers.StringRelatedField(
        many=True, read_only=True)
    
    class Meta:
        model = Restaurent
        fields = ['id', 'restaurent_photo', 'restaurent_name',
                  'restaurent_address', 'restaurent_schedule', 'restaurent_product']

class Restaurent_scheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurent_schedule
        fields = ['id', 'restaurents', 'opening_and_closing_days',
                  'opening_and_closing_hours']


class Product_sale_infoSerializer(serializers.ModelSerializer):
   
    time_of_the_day = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S")
    class Meta:
        model = Product_sale_info
        fields = ['id', 'day_of_the_week',
                  'time_of_the_day', 'restaurent_product']
        extra_kwargs = {'restaurent_product': {'required': False}}

class Restaurent_productSerializer(serializers.ModelSerializer):
    product_sale_info = Product_sale_infoSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurent_product
        fields = ['id', 'restaurent_product', 'product_photo', 'product_name',
                  'product_price', 'product_categories', 'description', 'promotional_price', 'on_sale', 'product_sale_info']
        extra_kwargs = {'product_sale_detail': {'required': False}}



