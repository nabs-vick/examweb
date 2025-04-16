from django.contrib import admin
from .models import Service, Order, Customer, Category 
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Service)
