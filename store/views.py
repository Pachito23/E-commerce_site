from django.shortcuts import render

# Create your views here.

def home(request):
     context = {}
     return render(request, 'home.html', context)

def store(request):
     context = {}
     return render(request, 'store.html', context)

def cart(request):
     context = {}
     return render(request, 'cart.html', context)

def checkout(request):
     context = {}
     return render(request, 'checkout.html', context)

def about(request):
     context = {}
     return render(request, 'about.html', context)