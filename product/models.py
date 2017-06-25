from django.db import models
from djmoney.models.fields import MoneyField



class Category(models.Model):
	category_id = models.IntegerField()
	name = models.CharField(max_length=50)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'


class Product(models.Model):
	product_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255, unique=True, )
	slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
	code = models.CharField(max_length=50, )
	price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	categories = models.ManyToManyField(Category)

	class Meta:
		ordering = ['-price']



class PriceList(models.Model):
	pass

class PriceListDetials(models.Model):
	pass
