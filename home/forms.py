from django import forms  # forms là module của Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking

class BookingForm(forms.ModelForm):  # forms.ModelForm là lớp cơ sở
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']