import os
from django.conf import settings
from django.shortcuts import render
from django import forms
from cart.cart import Cart
from .models import Order
from .models import OrderItem
#import weasyprint , os
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.template.loader import render_to_string
from cart.cart import Cart
from .models import Order
from .models import OrderItem

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name', 'email', 'address', 'postal_code', 'city']


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'order_completed.html', {'order': order})
    else:
        form = OrderCreateForm()
    
    return render(request, 'order_create.html' , {'cart':cart , 'form': form})
    
def order_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order_invoice.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=invoice_{order.id}.pdf'
    css_path = os.path.join(settings.STATIC_ROOT, 'invoice_pdf.css')
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(css_path)])
    return response


