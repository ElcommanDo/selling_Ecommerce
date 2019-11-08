from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST

#from coupon.forms import CouponApplyForm
from sell.models import Product
from .cart import Cart
from .forms import CartAddProductForm
@require_POST
def add(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    print(product)
    
    form = CartAddProductForm(request.POST)
  
    if form.is_valid():
             print("hello ")
             cd = form.cleaned_data
             cart.Add(
                product,
                cd['quantity'],
                cd['update']
                )
        
    return redirect('cart_details')
def delete(request,product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.delete(product)
    return redirect('cart_details')

def cart_details(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
    context = {'cart':cart}
    return render(request,'cart/cart_details.html',context)

