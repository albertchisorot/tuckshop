from django.db import models

# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False,default=0)

    def save(self, *args, **kwargs):
        # Calculate the total price before saving
        self.total_price = self.product.price * self.quantity

        # Update stock after a sale is saved
        if self.pk is None:  # If this is a new sale (not an update)
            product = self.product
            if product.stock >= self.quantity:
                product.stock -= self.quantity
                product.save()  # Save the updated stock
            else:
                raise ValueError("Not enough stock available.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sale of {self.product.name} on {self.date}"


class Bill(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description
