from django.db import models
from customer.models import Customer
from product.models import Product
from djmoney.models.fields import MoneyField

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
	customer_order_no = models.TextField(max_length='10')
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

	order_id = models.ForeignKey(SalesOrder, related_name='items', on_delete=models.CASCADE)
	product_name = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
	ordered_qty = models.IntegerField()
	delivered_qty = models.IntegerField()
	price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	note = models.TextField(max_length=50, blank=True)

	class meta:
		unique_together = ('sales_order_id', 'product_name')


	def total(self):
		pass

	def __str__(self):
		return '%s %s' %(self.order_id,self.product_name)

