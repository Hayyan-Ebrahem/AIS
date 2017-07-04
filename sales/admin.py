from django.contrib import admin
from sales.models import SalesOrder
from sales.models import SalesOrderDetails
# Register your models here.

admin.site.register(SalesOrder)
admin.site.register(SalesOrderDetails)
