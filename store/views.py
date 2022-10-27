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
     context = {}
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