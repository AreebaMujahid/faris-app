from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product,Review
# Create your views here.
from cart.views import CartAddProductForm
from django.shortcuts import render
from django.forms import ModelForm , Textarea
from .models import Product

def home(request):
    searchTerm = request.GET.get('searchProduct', '')
    if searchTerm:
        products = Product.objects.filter(name__icontains=searchTerm)
    else:
        products = Product.objects.all()

    nproduct = len(products)
    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'products': products,
        'nproduct': nproduct
    })

def detail(request, product_id):
     product = get_object_or_404(Product, pk= product_id)
     reviews= Review.objects.filter(product=product)
     cart_product_form = CartAddProductForm()

     return render(request,'detail.html',{'product':product , 'reviews':reviews,
                                          'cart_product_form': cart_product_form})

class ReviewForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model= Review
        fields= ['text']
        widgets= {'text': Textarea(attrs={'rows':5})}

@login_required
def createreview(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'GET':
        return render(request, 'createrreview.html', {'form': ReviewForm(), 'product': product})
    else:
        try:
            form= ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.product = product
            new_review.save()
            return redirect('detail' , new_review.product_id)
        except ValueError:
            return render(request, 'createreview.html',
                          {'form': ReviewForm(),'error':'Bad data passed in'})
        
@login_required
def deletereview(request,review_id):
    review= get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail',review.product.id)
