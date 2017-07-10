from django.contrib import admin
from customer.models import Customer
from customer.models import Category
from customer.models import CustomerCategory
# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(CustomerCategory)