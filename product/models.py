from django.db import models
from django.core.validators import MinValueValidator
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import HStoreField
from .managers import PandasDataFrameManager, PandasQuerySet
from pandas import DataFrame
import uuid

class Category(models.Model):
    #code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ProductClass(models.Model):
    name = models.TextField(max_length=10)
    slug = models.SlugField(max_length=20, unique=True, help_text='Unique value for product page URL, created from name.')
    product_code = models.CharField(max_length=10)
    has_variants = models.BooleanField(default=True)
    #price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    max_stock_level = models.PositiveIntegerField()
    min_stock_level = models.PositiveIntegerField()
    recorded_stock_level = models.PositiveIntegerField()

    def test_func(self):
        return 'HHHHHHHHHHHH'
    class Meta:
        abstract = True


    def __str__(self):
        return self.name

class Product(ProductClass):

    description = models.TextField(max_length=120)
    categories = models.ManyToManyField(Category,related_name='products')
    #price = MoneyField(max_digits=12, decimal_places=2)
    available_on = models.DateField(blank=True, null=True)
    attributes = HStoreField()
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        manager_inheritance_from_future = True 

    objects = models.Manager()
    analysis = PandasDataFrameManager()#.from_queryset(PandasQuerySet)()


    def get_absoulte_url(self):
        return reverse('products:detail', args=[str(self.slug)])


class ProductVariant(Product):
    sku = models.CharField(max_length=32, unique=True)
    #price_override = MoneyField(max_digits=12, decimal_places=2,blank=True, null=True)
    product = models.ForeignKey(Product, related_name='variants')
   
    

# class ProductCategories(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # discount = models.BooleanField(default=False)

    # class Meta:
    #   verbose_name_plural = 'Product Categories'

    # def __str__(self):
    #   return '%s-%s' %(self.product.name,self.category.code)

# class PriceList(models.Model):
#   code = models.CharField(max_length=10, unique=True)
#   description = models.TextField(max_length=20)
#   created_at = models.DateTimeField(auto_now_add=True)
#   validate_till = models.DateField()
#   blocked_till = models.DateField()
#   status = models.BooleanField(default=True)

#   def __str__(self):
#       return str(self.code)


# class PriceListDetial(models.Model):
#   price_list_code = models.ForeignKey(PriceList, related_name='price_code')
#   product_code = models.ForeignKey(Product, related_name='product')
#   product_unit = models.TextField(max_length=10)
#   unit_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

#   def __str__(self):
#       return '%s,%s' % (self.price_list_code, self.product_code)
