from django.contrib import admin
from .models import customer, products, Order

# Register your models here.
admin.site.register(customer)
admin.site.register(products)
admin.site.register(Order)
