from django.contrib import admin
from product.models import Product,Category,PriceList,PriceListDetial
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PriceList)
admin.site.register(PriceListDetial)