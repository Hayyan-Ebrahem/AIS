from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
#from product.models import PriceList


class Customer(models.Model):

	payment_terms = (
		('PIA','Payment in advance'),
		('EOM','End of the month'),
		('CWO','Ch with order'),
	)

	customer_id = models.AutoField(primary_key=True)

	customer_name = models.TextField(max_length=30)

	#customer_address = models.TextField(max_length=50)
	credit_limit = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	payment_term = models.TextField(max_length=50, choices=payment_terms, default='EOM')
	#price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)

	def __str__(self):
		return self.customer_name