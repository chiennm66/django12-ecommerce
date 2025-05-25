from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Product, Booking
from .forms import BookingForm
from .models import Product,Cart
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.contrib.sessions.models import Session
from .forms import SignUpForm

import logging

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ cơ sở dữ liệu
    return render(request, 'product_list.html', {'products': products})


def home(request):
    logger.info("Home view called")
    product_list = Product.objects.all().order_by('id')  # Sắp xếp theo id
    paginator = Paginator(product_list, 4)  # hiển thị 4 sản phẩm trên mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


#---------#


def product_detail(request, pk):
    logger.info(f"Product detail view called with pk={pk}")
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.product = product
            booking.save()
            logger.info(f"Booking created for product {product.name} by {booking.name}")
            return redirect('booking_success')  # Điều hướng đến trang thành công
    else:
        form = BookingForm()

    return render(request, 'product_detail.html', {'product': product, 'form': form})


def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)  # Hiển thị 6 sản phẩm mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product_list.html', {'page_obj': page_obj})


def contact(request):
    return render(request, 'contact.html')

def booking_success(request):
    return render(request, 'booking_success.html')

def signin(request):
    return render(request, 'signin.html')




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('signin') 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    return render(request, 'logoutaghh.html')

def add_to_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    session_key=request.session.session_key
    if not session_key:
        request.session.create()
        session_key=request.session.session_key
    cart_item, created=Cart.objects.get_or_create(
        product=product,
        session_key=session_key,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('view_cart')
def view_cart(request):
    session_key=request.session.session_key
    cart_items=Cart.objects.filter(session_key=session_key)
    total_price=sum(item.get_total_price() for item in cart_items)
    return render(request,'cart.html', {'cart_items':cart_items, 'total_price':total_price})

def remove_from_cart(request, item_id):
    session_key = request.session.session_key
    try:
        cart_item = Cart.objects.get(product_id=item_id, session_key=session_key)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('view_cart')