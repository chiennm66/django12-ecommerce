from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, product_detail, product_list, contact
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('products/', product_list, name='product_list'), 
    path('contact/', contact, name='contact'),  
    path('booking-success/', views.booking_success, name='booking_success'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/', views.view_cart, name="view_cart"),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin')
]