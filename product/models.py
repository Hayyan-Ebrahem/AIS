from django.db import models
#from djmoney.models.fields import MoneyField

class Category(models.Model):
	category_code = models.CharField(max_length=10, unique=True)
	name = models.CharField(max_length=20)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20, unique=True, )
	slug = models.SlugField(max_length=20, unique=True, help_text='Unique value for product page URL, created from name.')
	product_code = models.CharField(max_length=10)
	price = models.IntegerField()
	category_code = models.ForeignKey(Category)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	#warehouse_code = models.ForeignKey(warehouse)
	max_stock_level = models.DecimalField(max_digits=5, decimal_places=2)
	min_stock_level = models.DecimalField(max_digits=5, decimal_places=2)
	recorded_stock_level = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		ordering = ['-price']

	def __str__(self):
		return self.name


	def getlist(self):
		return self.price*12


class PriceList(models.Model):
	price_list_code = models.AutoField(primary_key=True)
	description = models.TextField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	validate_till = models.DateField()
	blocked_till = models.DateField()
	status = models.BooleanField(default=True)

	def __str__(self):
		return str(self.price_list_code)


class PriceListDetial(models.Model):
	price_list_code = models.ForeignKey(PriceList)
	product_code = models.ForeignKey(Product)
	product_unit = models.TextField(max_length=10)
	unit_price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return '%s,%s' % (self.price_list_code, self.product_code)