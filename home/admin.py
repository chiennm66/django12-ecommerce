from django.contrib import admin
from .models import Product
from .models import Booking

admin.site.register(Product)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'email', 'phone', 'booking_date')
    search_fields = ('name', 'email', 'phone', 'product__name')
    list_filter = ('booking_date',)