from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('sign_in/', views.sign_in, name = "sign_in"),
    path('sign_up/', views.sign_up, name = "sign_up"),
    path('process_logout/', views.process_logout, name = "process_logout"),
    path('store/', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('shipping/', views.shipping, name = "shipping"),
    path('payment/', views.payment, name = "payment"),
    path('about/', views.about, name = "about"),
    path('sleeping_bags/',views.sleeping_bags, name="sleeping_bags"),
    path('jackets/',views.jackets, name="jackets"),
    path('accessories/',views.accessories, name="accessories"),
    path('sales/', views.sales, name="sales"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('thank_you/',views.thank_you, name="thank_you"),
    path('process_order/',views.ProcessOrder, name="process_order"),
    path('process_payment/',views.ProcessPayment, name="process_payment"),
]
