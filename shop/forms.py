from django import forms
from .models import Product, Sale, Bill

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if product and quantity > product.stock:
            raise forms.ValidationError(f"Insufficient stock for {product.name}. Available stock: {product.stock}")
        return quantity

    def save(self, commit=True):
        sale = super().save(commit=False)
        product = sale.product
        # Calculate total price
        sale.total_price = product.price * sale.quantity
        if commit:
            sale.save()
        return sale

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['description', 'amount']
