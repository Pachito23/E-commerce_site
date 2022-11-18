from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import json
import datetime

# Create your views here.

def home(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
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
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'products': products, 'items':items, 'order':order}
     return render(request, 'store.html', context)


def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
          is_authenticated=True
     else:
          items=[]
          order=[]
          is_authenticated=False
     context = {'items':items, 'order':order, 'is_authenticated':is_authenticated}
     return render(request, 'cart.html', context)


def shipping(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          return redirect('store')
     context = {'items':items, 'order':order}
     return render(request, 'shipping.html', context)


def sleeping_bags(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'products': products,'items':items, 'order':order}
     return render(request, 'sleeping_bags.html', context)


def jackets(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'products': products,'items':items, 'order':order}
     return render(request, 'jackets.html', context)


def sales(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'products': products,'items':items, 'order':order}
     return render(request, 'sales.html', context)


def accessories(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'products': products,'items':items, 'order':order}
     return render(request, 'accessories.html', context)


def payment(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          return redirect('store')
     context = {'items':items, 'order':order}
     return render(request, 'payment.html', context)


def about(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'about.html', context)


def sign_in(request, attempted = False, login_failed=False, sign_up_ok = True, errors = None, created = False):
     if request.method == 'POST':
          if not request.user.is_authenticated:
               curr_username = request.POST['username']
               curr_password = request.POST['password']
               curr_user = authenticate(username = curr_username, password = curr_password)
               if curr_user is not None:
                    login(request, curr_user)
                    print('User has been authenticated')
                    attempted = True
                    
               else:
                    print('User has not been authenticated')
                    attempted=True
                    login_failed=True
          
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          customer = None
          items=[]
          order=[]
     
     context = {'customer':customer, 'items':items, 'order':order, 'is_authenticated':request.user.is_authenticated, 'attempted':attempted, 'login_failed':login_failed, 'sign_up_ok':sign_up_ok, 'errors':errors, 'created':created}
     return render(request, 'sign_in.html', context)

def sign_up(request, attempted = False, login_failed=False, sign_up_ok = True, errors = None, created = False):
     if request.method == 'POST':
          if not request.user.is_authenticated:
               curr_username = request.POST['Username']
               curr_password = request.POST['Password']
               curr_full_name = request.POST['Full_name']
               curr_email = request.POST['Email']
               sign_up_ok=True
               errors = ''

               try:
                    validate_password(curr_password, user=None, password_validators=None)
                    curr_user = User.objects.create_user(username = curr_username, password = curr_password)
               except ValidationError as e1:
                    sign_up_ok=False
                    for error in e1:
                         errors += error + ' '
               except IntegrityError as e2:
                    sign_up_ok=False
                    errors += "Username already exists." + ' '

               if sign_up_ok:
                    curr_user.save()
                    customer =Customer.objects.create(
                    user=curr_user,
                    full_name = curr_full_name,
                    email = curr_email
                    )
                    customer.save()
                    created=True
          
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          customer = None
          items=[]
          order=[]
     
     context = {'customer':customer, 'items':items, 'order':order, 'is_authenticated':request.user.is_authenticated, 'attempted':attempted, 'login_failed':login_failed, 'sign_up_ok':sign_up_ok, 'errors':errors, 'created': created}
     return render(request, 'sign_in.html', context)

def process_logout(request):
     data = json.loads(request.body)
     print(data)
     if data['log_out']:
          logout(request)
     return JsonResponse('Sign in info saved',safe=False)


def updateItem(request):
     data = json.loads(request.body)
     productId= data['productId']
     action= data['action']
     
     print('action:',action)
     print('productId:',productId)

     customer = request.user.customer
     product = Product.objects.get(id =productId)
     order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)

     orderItem,created =OrderItem.objects.get_or_create(order = order, product=product)

     if action == 'add':
          orderItem.quantity = (orderItem.quantity + 1)
     elif action == 'remove':
          orderItem.quantity = (orderItem.quantity - 1)
     elif action == 'delete':
          orderItem.quantity = 0
     
     orderItem.save()
     
     if orderItem.quantity <= 0:
          orderItem.delete()


     return JsonResponse('Item was added',safe=False)


def ProcessOrder(request):
     data = json.loads(request.body)

     if request.user.is_authenticated:
          customer=request.user.customer
          print(data)
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          total=float(data['form']['total'])

          if total == order.cart_total_final_price:
               order.complete = True

          shipping = Shipping.objects.create(
               customer = customer,
               order = order,
               address = data['shipping']['address'],
               city = data['shipping']['city'],
               comments = data['shipping']['comments'],
               country = data['shipping']['country'],
               zipcode = data['shipping']['zip'],
          )

          order.update_shipping(shipping)

          order.save()

     else:
          print('User is not authenticated')

     return JsonResponse('Shipping info saved',safe=False)


def ProcessPayment(request):
     transaction_id = datetime.datetime.now().timestamp()
     data = json.loads(request.body)

     if request.user.is_authenticated:
          customer=request.user.customer
          print(data)
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          order.transaction_id = transaction_id
          order.payment_confirmation = True

          payment_info = Payment.objects.create(
               customer = customer,
               card_number = data['payment']['card_num'],
               card_holder_name = data['payment']['card_name'],
               expiration = data['payment']['exp'],
               cvv = data['payment']['cvv'],
          )

          order.update_payment(payment_info)

          order.save()
          
     else:
          print('User is not authenticated')

     return JsonResponse('Payment info saved',safe=False)


def thank_you(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order,created = Order.objects.get_or_create(customer=customer,payment_confirmation = False)
          items =order.orderitem_set.all()
     else:
          items=[]
          order=[]
     context = {'items':items, 'order':order}
     return render(request, 'thank_you.html', context)