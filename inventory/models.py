from django.db import models
from django.conf import settings
# Create your models here.

class WarehouseCategory(models.Model):
	code = models.TextField(primary_key=True, max_length=30)
	name = models.TextField(max_length=30, unique=True)
	created_at = models.DateField(auto_now_add=True)
	user_id = models.TextField(max_length=15)
	#should be related to user table will be done later

class Warehouse(models.Model):
	code = models.TextField(primary_key=True, max_length=30)
	name = models.TextField(max_length=30, unique=True)
	location = models.TextField(max_length=50)
	#chart_of_account_no = models.ForeignKey(ChartOfAccountNo, on_delete=models.CASCADE)
	category = models.ForeignKey(WarehouseCategory, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)
	user_id = models.TextField(max_length=15)
	#should be related to user table will be done later
	warehouse_keeper_id = models.TextField(max_length=15)
	#should be related to user table will be done later