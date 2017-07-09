from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
#from product.models import PriceList

class CustomerCategory(models.Model):

	code = models.TextField(primary_key=True, max_length=30)
	name = models.TextField(max_length=50, unique=True)
	created_at = models.DateField(auto_now_add=True)
	#should be related to user table will be done later
	user_id = models.TextField(max_length=15)
	#should be related to user table will be done later

	def __str__(self):
		return self.name

class Customer(models.Model):

	payment_terms = (
		('PIA','Payment in advance'),
		('EOM','End of the month'),
		('CWO','Chash with order'),
	)

	shipping_terms = (
		('CIF', 'Cost, Insurance and Freight'), 
		('COP','Customs of the Port'), 
		('DWT','Deadweight Tonnage'),
	)

	code = models.TextField(primary_key=True, max_length=30)
	name = models.TextField(max_length=30, unique=True)
	address = models.TextField(max_length=50)
	phone_no = models.TextField(max_length=30, unique=True)
	email = models.TextField(max_length=30, unique=True)
	category_code = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE)
	chart_of_account = models.TextField(max_length=30)
	credit_limit = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	credit_period = models.DateField()
	payment_term = models.CharField(max_length=50, choices=payment_terms, default='EOM')
	shipping_term = models.CharField(max_length=50, choices=shipping_terms, default='CIF')
	ref_document_no = models.TextField(max_length=10)
	ref_document_date = models.DateField()
	user_id = models.TextField(max_length=15)
	#should be related to user table will be done later
	created_at = models.DateField(auto_now_add=True)
	sales_man_id = models.TextField(max_length=15)
	#should be related to user table will be done later
	status = models.BooleanField()
	#if 0 the status will appear Blocked, if 1 the status will appear active
	active_till_date = models.DateField()
	blocked_till_date = models.DateField()
	#price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


