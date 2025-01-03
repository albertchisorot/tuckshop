from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Sale, Bill
from .forms import ProductForm, SaleForm, BillForm

# Dashboard View
def dashboard(request):
    total_sales = sum(sale.total_price for sale in Sale.objects.all())
    total_bills = Bill.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    profit = total_sales - total_bills
    total_products = Product.objects.aggregate(Sum('stock'))['stock__sum'] or 0

    context = {
        'total_sales': total_sales,
        'total_bills': total_bills,
        'profit': profit,
        'total_products': total_products,
    }
    return render(request, 'dashboard.html', context)

# Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Add Product View
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# Edit Product View
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

# Delete Product View
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')
# Sale List View
def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales_list.html', {'sales': sales})

# Add Sale View
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # This will update stock and save the sale
                return redirect('sales_list')
            except ValueError as e:
                form.add_error(None, str(e))  # Add the error if stock is insufficient
    else:
        form = SaleForm()
    return render(request, 'add_sale.html', {'form': form})

# Edit Sale View
def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'edit_sale.html', {'form': form})

# Delete Sale View
def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.delete()
    return redirect('sales_list')

# Bill List View
def bills_list(request):
    bills = Bill.objects.all()
    return render(request, 'bills_list.html', {'bills': bills})

# Add Bill View
def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bills_list')
    else:
        form = BillForm()
    return render(request, 'add_bill.html', {'form': form})

# Edit Bill View
def edit_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bills_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'edit_bill.html', {'form': form})

# Delete Bill View
def delete_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    bill.delete()
    return redirect('bills_list')
