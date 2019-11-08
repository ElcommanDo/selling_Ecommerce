from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm
# Create your views here.
def home(request):
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    context = {'products':products,'cart_product_form':cart_product_form} 
    return render(request,'sell/index.html',context)


def product_details(request,id,slug):
    product = Product.objects.get(id=id,slug=slug)
    cart_product_form = CartAddProductForm()
    context = {'product':product,'cart_product_form':cart_product_form}
    return render(request,"sell/product_details.html",context)
