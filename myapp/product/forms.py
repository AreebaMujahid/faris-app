
# myapp/product/forms.py

# product/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Email or Username"
        self.fields['username'].widget.attrs.update({'autofocus': True, 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'availability', 'url', 'image']
