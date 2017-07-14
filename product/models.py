from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator
import uuid

class Category(models.Model):
	#code = models.CharField(max_length=10, unique=True)
	name = models.CharField(max_length=20)
	description = models.TextField(max_length=50, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)

	@property
	def code(self):
		return '%s-%s' %(self.id,self.name)

	class Meta:
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Product(models.Model):
	product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(max_length=10)
	slug = models.SlugField(max_length=20, unique=True, help_text='Unique value for product page URL, created from name.')
	product_code = models.CharField(max_length=10)
	categories = models.ManyToManyField(Category, related_name='products')
	price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	#warehouse_code = models.ForeignKey(warehouse)
	max_stock_level = models.PositiveIntegerField()
	min_stock_level = models.PositiveIntegerField()
	recorded_stock_level = models.PositiveIntegerField()

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.name

# class ProductCategories(models.Model):
	# product = models.ForeignKey(Product, on_delete=models.CASCADE)
	# category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# discount = models.BooleanField(default=False)

	# class Meta:
	# 	verbose_name_plural = 'Product Categories'

	# def __str__(self):
	# 	return '%s-%s' %(self.product.name,self.category.code)

# class PriceList(models.Model):
# 	code = models.CharField(max_length=10, unique=True)
# 	description = models.TextField(max_length=20)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	validate_till = models.DateField()
# 	blocked_till = models.DateField()
# 	status = models.BooleanField(default=True)

# 	def __str__(self):
# 		return str(self.code)


# class PriceListDetial(models.Model):
# 	price_list_code = models.ForeignKey(PriceList, related_name='price_code')
# 	product_code = models.ForeignKey(Product, related_name='product')
# 	product_unit = models.TextField(max_length=10)
# 	unit_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

# 	def __str__(self):
# 		return '%s,%s' % (self.price_list_code, self.product_code)