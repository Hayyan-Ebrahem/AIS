from django.contrib import admin
from inventory.models import Warehouse, WarehouseCategory
# Register your models here.

admin.site.register(Warehouse)
admin.site.register(WarehouseCategory)