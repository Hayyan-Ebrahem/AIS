from django.contrib import admin
from sales.models import SalesOrder, SalesOrderDetails
# Register your models here.

admin.site.register(SalesOrder)
admin.site.register(SalesOrderDetails)

