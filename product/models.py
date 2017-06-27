from django.db import models
#from djmoney.models.fields import MoneyField



class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
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
	name = models.CharField(max_length=255, unique=True, )
	slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
	code = models.CharField(max_length=50)
	price = models.IntegerField()
	categories = models.ManyToManyField(Category, related_name='products')

	class Meta:
		ordering = ['-price']
#

	def __str__(self):
		return self.name

	def getlist(self):
		return self.price*12

class PriceList(models.Model):
	pass

class PriceListDetials(models.Model):
	pass
