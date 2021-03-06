from django.db import models


PRODUCT_CATEGORIES = [
        ('SWEET', 'Sweet'),
        ('SAVORY', 'Savory'),
        ('JUICE', 'Juice'),
]

# Create your models here.
class Restaurent(models.Model):
  restaurent_photo = models.ImageField(upload_to='blog/%Y/%m/%d')
  restaurent_name = models.CharField(('Restaurant name'), max_length=120, default="")
  restaurent_address = models.TextField(('Restaurant address'), max_length=120, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = ("Restaurent")
    verbose_name_plural = ("Restaurents")



class Restaurent_schedule(models.Model):
    # restaurents = models.ManyToManyField(Restaurent)
    restaurents = models.ForeignKey(
        Restaurent, on_delete=models.CASCADE, related_name='restaurent_schedule')
    opening_and_closing_days = models.CharField(('Opening and closing days'), max_length=120, default="")
    opening_and_closing_hours = models.CharField(('Opening and closing hours'), max_length=120, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = ("Restaurent schedule")
        verbose_name_plural = ("Restaurent schedules")

    def __str__(self):
        return self.opening_and_closing_days

class Restaurent_product(models.Model):
    restaurent_product = models.ForeignKey(
        Restaurent, on_delete=models.CASCADE, related_name='restaurent_product', null=True)
    product_photo = models.ImageField(upload_to='blog/%Y/%m/%d')
    product_name = models.CharField(("Product Name"), max_length=100, blank=True)
    product_price = models.FloatField(('Product price'), default="")
    product_categories = models.CharField(('Product Categories'), max_length=120, default="", choices=PRODUCT_CATEGORIES)
    description =  models.TextField(('Description'), max_length=120, default="")
    promotional_price = models.IntegerField(('Promotional Price'))
    on_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = ("Restaurent product")
        verbose_name_plural = ("Restaurent products")


class Product_sale_info(models.Model):
    restaurent_product = models.ManyToManyField(
        Restaurent_product, related_name="product_sale_info", blank=True)
    day_of_the_week = models.CharField(('Product price'), max_length=120, default="")
    time_of_the_day = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Product sale information")
        verbose_name_plural = ("Product sale informations")
