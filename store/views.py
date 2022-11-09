from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'home.html', context)

def store(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'products': products, 'items':items, 'order':order}
     return render(request, 'store.html', context)

def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'cart.html', context)

def shipping(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'shipping.html', context)

def payment(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'payment.html', context)

def about(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'about.html', context)

def updateItem(request):
     data = json.loads(request.body)
     productId= data['productId']
     action= data['action']
     
     print('action:',action)
     print('productId:',productId)

     customer = request.user.customer
     product = Product.objects.get(id =productId)
     order,created = Order.objects.get_or_create(customer=customer,complete = False)

     orderItem,created =OrderItem.objects.get_or_create(order = order, product=product)

     if action == 'add':
          orderItem.quantity = (orderItem.quantity + 1)
     elif action == 'remove':
          orderItem.quantity = (orderItem.quantity - 1)
     
     orderItem.save()
     
     if orderItem.quantity <= 0:
          orderItem.delete()


     return JsonResponse('Item was added',safe=False)

def thank_you(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,complete = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'thank_you.html', context)