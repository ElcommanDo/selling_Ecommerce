from django.urls import path
from . import views
urlpatterns = [
    path('cart_add/<int:product_id>/',views.add,name='cart_add'),
    path('cart_delete/<int:product_id>/',views.delete,name='cart_delete'),
    path('cart_details',views.cart_details,name='cart_details'),



]
