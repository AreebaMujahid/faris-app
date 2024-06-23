from django import forms

class CartUpdateProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, initial=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)