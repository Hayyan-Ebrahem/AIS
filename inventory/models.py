from django.db import models
from django.conf import settings
# Create your models here.

class Category(models.Model):
	code = models.TextField(primary_key=True, max_length=30)
	name = models.TextField(max_length=30, unique=True)
	created_at = models.DateField(auto_now_add=True)
	user_id = models.TextField(max_length=15)
	#should be related to user table will be done later

	class metta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Warehouse(models.Model):
	code = models.TextField(primary_key=True, max_length=30)
	name = models.TextField(max_length=30, unique=True)
	location = models.TextField(max_length=50)
	#chart_of_account_no = models.ForeignKey(ChartOfAccountNo, on_delete=models.CASCADE)
	category_code = models.ManyToManyField(Category, through='WarehouseCategory')
	created_at = models.DateField(auto_now_add=True)
	user_id = models.TextField(max_length=15)
	#should be related to user table will be done later
	warehouse_keeper_id = models.TextField(max_length=15)
	#should be related to user table will be done later

	def __str__(self):
		return self.name

class WarehouseCategory(models.Model):
	warehouse_code = models.ForeignKey(Warehouse)
	category_code = models.ForeignKey(Category)

	def __str__(self):
		return 'Category'