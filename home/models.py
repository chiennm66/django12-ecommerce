from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=10)  # Thêm giá trị mặc định
    trailer_url = models.URLField(blank=True, null=True)  # Link YouTube hoặc video khác


class Booking(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Tên người đặt vé
    email = models.EmailField()  # Email người đặt vé
    phone = models.CharField(max_length=15)  # Số điện thoại
    booking_date = models.DateTimeField(auto_now_add=True)  # Ngày đặt vé


class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    session_key=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    def get_total_price(self):
        return self.quantity * self.product.price
def __str__(self):
    return f"Booking for {self.product.name} by {self.name}"
def __str__(self):
    return self.name

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('product_detail', args=[str(self.id)])

class Seat(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

class BookingSeat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)