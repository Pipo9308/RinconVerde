# cart/forms.py
from django import forms
from .models import Product

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1, initial=1)

    def clean_quantity(self):
        product_id = self.cleaned_data.get('product_id')
        quantity = self.cleaned_data['quantity']
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise forms.ValidationError("Invalid product.")
        
        if quantity > product.stock:
            raise forms.ValidationError(f"Only {product.stock} units available in stock.")
        
        return quantity
