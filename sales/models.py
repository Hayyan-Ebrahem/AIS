from django.db import models
from customer.models import Customer
from product.models import Product
from django.conf import settings
#from djmoney.models.fields import MoneyField

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

	sale_order_id  = models.AutoField(primary_key=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	customer_order_no = models.IntegerField()
	customer_order_date = models.DateTimeField()
	payment_term = models.TextField(max_length=50, choices=payment_terms, default='EOM')
	#shipment_term = models.TextField(max_length=50, choices=payment_terms,default=EOM)
	#price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)
	create_date = models.DateTimeField()
	status = models.TextField(choices=status_choices, default='WIP')
	#sales_order_items = models.ManyToManyField(Product, 
    #    through='SalesOrderDetails')
   
	def compute_amount_all(self):
		"""
		Compute the total amount of the SaleOrder
		"""
		pass


	def __str__(self):
		return self.customer


class SalesOrderDetails(models.Model):


	sales_order_id = models.ForeignKey(SalesOrder, related_name='lines', on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_unit = models.IntegerField()
	unit_price = models.IntegerField()
	ordered_qty = models.DecimalField(max_digits=5, decimal_places=2)
	delivered_qty = models.DecimalField(max_digits=5, decimal_places=2)
	note = models.TextField(max_length=200)

	class meta:
		unique_together = ('sales_order_id', 'product_id')


	def total(self):
		pass

	def __str__(self):
		return (str(self.sales_order_id), str(self.product_id))

