from itertools import product
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
     context = {}
     return render(request, 'home.html', context)

def store(request):
     products = Product.objects.all()
     context = {'products': products}
     return render(request, 'store.html', context)

def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
     context = {'items':items, 'order':order}
     return render(request, 'cart.html', context)

def shipping(request):
     context = {}
     return render(request, 'shipping.html', context)

def payment(request):
     context = {}
     return render(request, 'payment.html', context)

def about(request):
     context = {}
     return render(request, 'about.html', context)