from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.models.fields import PositiveSmallIntigerFeild
#from product.models import PriceList


class Customer(models.Model):

	payment_terms = (
		('PIA','Payment in advance'),
		('EOM','End of the month'),
		('CWO','Ch with order'),
	)

	id = models.AutoField(primary_key=True)
	name = models.TextField(max_length=30)
	address = models.TextField(max_length=50)
	phone_no = models.TextField(max_length=10)
	email = models.TextField(max_length=30)
	category_id = models.PositiveSmallIntigerFeild() 
	credit_limit = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	credit_periosd = models.
	payment_term = models.TextField(max_length=50, choices=payment_terms, default='EOM')
	#price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)

	def __str__(self):
		return self.customer_name