from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('store/', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('shipping/', views.shipping, name = "shipping"),
    path('payment/', views.payment, name = "payment"),
    path('about/', views.about, name = "about"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('thank_you/',views.thank_you, name="thank_you"),
]
