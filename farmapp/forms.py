from django import forms
from .models import Order
from django.utils import timezone

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['price']
        # fields = '__all__'
        # fields = ['farmer_phone', 'from_name', 'from_phone', 'to_name', 'to_phone', 'to_address', 'quantity', 'grade']

class DateSearchForm(forms.Form):
    search_date = forms.CharField(label='날짜', initial=str(timezone.now())[:10])
