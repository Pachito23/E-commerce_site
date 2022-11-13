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
    name = models.CharField(max_length = 30,null=True)
    email = models.CharField(max_length = 50,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    type = models.CharField( max_length=30, blank = False,choices = [("Sleeping bag","Sleeping bag"),("Jacket","Jacket"),("Accessory","Accessory")])
    sale = models.BooleanField(default = False, null = True, blank = False)
    discount = models.IntegerField("% of discount", null = True, blank = False, default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    image = models.ImageField(null = True, blank = False)
    
    @property
    def sleeping_bag(self):
        if self.type == "Sleeping bag":
            return True
        else:
            return False
    
    @property
    def jacket(self):
        if self.type == "Jacket":
            return True
        else:
            return False

    @property
    def accessory(self):
        if self.type == "Accessory":
            return True
        else:
            return False


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


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank = True, null = True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=20,null=True)
    comments = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=20,null=True)
    zipcode = models.CharField(max_length=20,null=True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address


class Payment(models.Model):
    card_number = models.CharField(max_length=30,null=True, blank = True)
    card_holder_name = models.CharField(max_length=30,null=True, blank = True)
    expiration = models.DateTimeField(auto_now_add = True)
    cvv = models.CharField(max_length=3,null=True, blank = True)

    def __str__(self):
        return '**** **** **** ' + str(self.card_number[-4:])


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    #complete = False => Open cart => continue add items to the cart
    #complete = True => Closed cart => no items can be added to the cart
    complete = models.BooleanField(default = False, null = True, blank = True)
    transaction_id = models.CharField(max_length=50,null=True,blank=True)
    payment_confirmation = models.BooleanField(default = False, null = True, blank = False)
    shipping = models.ForeignKey(Shipping, on_delete=models.SET_NULL, blank = True, null = True)
    card_data = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return 'Order nr ' + str(self.id)

    def update_shipping(self, shipping_data):
        if self.shipping is not None:
            self.shipping.delete()
        self.shipping=shipping_data

    @property
    def empty(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.quantity for item in orderitems])
        if total==0:
            return True
        else:
            return False

    @property
    def delivery_date1(self):
        return datetime.datetime.now() + datetime.timedelta(days = 7)

    @property
    def delivery_date2(self):
        return datetime.datetime.now() + datetime.timedelta(days = 14)


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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE, blank = True, null = True)
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

    def __str__(self):
        return self.product.name