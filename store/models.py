# Create your models here.

from datetime import datetime
from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    size = models.CharField(default = ("N/a","N/a"), max_length=10, choices = [("N/a","N/a"),("XXS","XXS"),("XS","XS"),("S","S"),("M","M"),("L","L"),("XL","XL"),("XXL","XXL")])
    sale = models.BooleanField(default = False, null = True, blank = False)
    discount = models.IntegerField("% of discount", null = True, blank = False, default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    image = models.ImageField(null = True, blank = False)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def final_price(self):
        if self.sale:
            return self.price-(self.price*self.discount/100)
        else:
            return self.price
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    #complete = False => Open cart => continue add items to the cart
    #complete = True => Closed cart => no items can be added to the cart
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def delivery_date1(self):
        return self.date_ordered.date() + datetime.timedelta(days = 7)

    @property
    def delivery_date2(self):
        return self.date_ordered.date() + datetime.timedelta(days = 14)


    @property
    def cart_total_elements(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.quantity for item in orderitems])
        return total

    @property
    def cart_total_price(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.get_total_price for item in orderitems])
        return total

    @property
    def cart_total_final_price(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.get_total_final_price for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default=0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def get_total_final_price(self):
        total = self.product.final_price() * self.quantity
        return total

    @property
    def get_total_price(self):
        total = self.product.price * self.quantity
        return total

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    zipcode = models.CharField(max_length=20,null=True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address