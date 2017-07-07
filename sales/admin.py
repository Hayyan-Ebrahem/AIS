from django.contrib import admin
from sales.models import SalesOrder, SalesOrderDetail
# Register your models here.

admin.site.register(SalesOrder)
admin.site.register(SalesOrderDetail)

