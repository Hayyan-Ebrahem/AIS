from django.db import models
from customer.models import Customer
from product.models import Product,PriceList

from django.conf import settings
from djmoney.models.fields import MoneyField

class SalesOrder(models.Model):

	payment_terms = (
		('PIA','Payment in advance'),
		('EOM','End of the month'),
		('CWO','Cash with order'),
	)

	status_choices=(
		('WIP','working in process'),
		('INVOICED','invoiced'),

	)

	sale_order_id  = models.IntegerField(primary_key=True)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	customer_order_no = models.IntegerField()
	customer_order_date = models.DateTimeField()
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	payment_term = models.TextField(max_length=50, choices=payment_terms, default='EOM')
	#shipment_term = models.TextField(max_length=50, choices=payment_terms,default=EOM)
	price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)
	create_date = models.DateTimeField()
	customer = models.CharField(max_length=40)
	status = models.IntegerField(choices=status_choices, default='WIP')
   

	def __str__(self):
		return self.customer


class SalesOrderDetails(models.Model):


	sales_order_no = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	#product_unit = models.IntegerField()
	unit_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	ordered_qty = models.DecimalField(max_digits=5, decimal_places=2)
	delivered_qty = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return (str(self.sales_order_no), str(self.product_id))

