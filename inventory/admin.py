from django.contrib import admin
from inventory.models import Warehouse, WarehouseCategory, Category
# Register your models here.

admin.site.register(Warehouse)
admin.site.register(WarehouseCategory)
admin.site.register(Category)