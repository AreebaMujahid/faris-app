from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django import forms
from product.models import Product
from .cart import Cart
from .forms import CartUpdateProductForm
# Create your views here.
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(coerce=int,
                                      choices=[(i,str(i)) for i in range(1,51)])
    override = forms.BooleanField(required=False, initial=False,
                                  widget=forms.HiddenInput)
    


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial=
                                                         {'quantity': item['quantity'],
                                                          'override': True} )
    return render(request,'cart_detail.html', {'cart':cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # Determine if the form is for adding or updating quantity
    
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product, id=product_id)
    cart.remove(product)
    if len(cart) == 0:
        return redirect('home')
    else:
        return redirect('cart:cart_detail')
