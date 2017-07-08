from django.db import models
from customer.models import Customer
from product.models import Product
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
	customer_order_no = models.AutoField(unique=True)
	customer_order_date = models.DateTimeField()
	payment_term = models.CharField(max_length=5, choices=payment_terms, default='EOM')
	#shipment_term = models.TextField(max_length=50, choices=payment_terms,default=EOM)
	#price_list_code = models.ForeignKey(PriceList, related_name='price_list', on_delete=models.CASCADE)
	create_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=5, choices=status_choices, default='WIP')
	#sales_order_items = models.ManyToManyField(Product, 
    #    through='SalesOrderDetails')

	def __str__(self):
		return str(self.sale_order_id)


class SalesOrderDetail(models.Model):

	order_id = models.ForeignKey(SalesOrder, related_name='lines', on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
	product_unit = models.IntegerField()
	#unit_price = models.IntegerField()
	ordered_qty = models.IntegerField()
	delivered_qty = models.IntegerField()
	note = models.TextField(max_length=200)

	class meta:
		unique_together = ('sales_order_id', 'product_id')


	def total(self):
		pass

	def __str__(self):
		return (str(self.sales_order_id), str(self.product_id))

