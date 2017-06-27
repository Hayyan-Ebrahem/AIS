from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
from product.models import PriceList


class Customer(models.Model):

	payment_terms = (
		('PIA','Payment in advance'),
		('EOM','End of the month'),
		('CWO','Cash with order'),
	)


	customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	credit_limit = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	payment_term = models.TextField(max_length=50, choices=payment_terms, default='EOM')
	price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)

	def __str__(self):
		return self.customer