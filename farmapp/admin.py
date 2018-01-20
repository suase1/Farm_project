from django.contrib import admin
from farmapp.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('farmer_phone','from_name','from_phone',
    'to_name','to_phone','to_address','quantity','grade','price','order_date')
    list_filter = ('farmer_phone','order_date')

admin.site.register(Order, OrderAdmin)
