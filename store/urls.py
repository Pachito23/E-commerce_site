from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('store/', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('shipping/', views.shipping, name = "shipping"),
    path('payment/', views.payment, name = "payment"),
    path('about/', views.about, name = "about"),
]
