from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Restaurent)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['restaurent_photo', 'restaurent_name', 'restaurent_address']

@admin.register(Restaurent_schedule)
class Restaurent_scheduleAdmin(admin.ModelAdmin):
 list_display = ['opening_and_closing_days', 'opening_and_closing_hours']


@admin.register(Restaurent_product)
class Restaurent_productAdmin(admin.ModelAdmin):
 list_display = ['product_name', 'product_photo',
                 'product_price', 'product_categories', 'description', 'promotional_price', 'on_sale']


@admin.register(Product_sale_info)
class Product_sale_infoAdmin(admin.ModelAdmin):
 list_display = ['day_of_the_week', 'time_of_the_day']
