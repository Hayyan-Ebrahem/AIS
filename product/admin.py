from django.contrib import admin
from product.models import Product,Category,ProductCategory
# Register your models here.


class MembershipInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','code')
	inlines = [
        MembershipInline,
    ]



admin.site.register(Product, ProductAdmin)
#admin.site.register(Category, ProductAdmin)