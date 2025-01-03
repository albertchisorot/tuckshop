from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Product CRUD
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),

    # Sale CRUD
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/add/', views.add_sale, name='add_sale'),
    path('sales/edit/<int:pk>/', views.edit_sale, name='edit_sale'),
    path('sales/delete/<int:pk>/', views.delete_sale, name='delete_sale'),

    # Bill CRUD
    path('bills/', views.bills_list, name='bills_list'),
    path('bills/add/', views.add_bill, name='add_bill'),
    path('bills/edit/<int:pk>/', views.edit_bill, name='edit_bill'),
    path('bills/delete/<int:pk>/', views.delete_bill, name='delete_bill'),
]
