from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.db.models.functions import Concat
import datetime
from datetime import timedelta


# from product.models import PriceList

class Category(models.Model):
    code = models.TextField(primary_key=True, max_length=30)
    name  = models.TextField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    # should be related to user table will be done later
    user_id = models.TextField(max_length=15)
    # should be related to user table will be done later

    class meta:
    	verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Customer(models.Model):
    payment_terms = (
        ('PIA', 'Payment in advance'),
        ('EOM', 'End of the month'),
        ('CWO', 'Cash with order'),
    )

    shipping_terms = (
        ('CIF', 'Cost, Insurance and Freight'),
        ('COP', 'Customs of the Port'),
        ('DWT', 'Dead weight Tonnage'),
    )

    first_period = datetime.timedelta(days=30)
    second_period = datetime.timedelta(days=60)
    third_period = datetime.timedelta(days=90)

    duration_choices = ((first_period, '30'), (second_period, '60'), (third_period, '90'))

    first_choice = 'day'
    second_choice = 'month'
    third_choice = 'year'

    period_choices=((first_choice, 'day'), (second_choice, 'month'), (third_choice, 'year'))

    code = models.CharField(primary_key=True, max_length=10)
    name = models.TextField(max_length=10, unique=True)
    address = models.TextField(max_length=20)
    phone_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    category_code = models.ManyToManyField(Category,through='CustomerCategory')
    # chart_of_account_no = models.TextField(max_length=30)
    credit_limit = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    period_unit = models.TextField(choices=period_choices, default=first_choice)
    credit_period = models.DurationField(choices=duration_choices, default=first_period)
    #need to check how to add duration unit??
    payment_term = models.CharField(max_length=50, choices=payment_terms, default='EOM')
    shipping_term = models.CharField(max_length=50, choices=shipping_terms, default='CIF')
    ref_document_no = models.TextField(max_length=10)
    ref_document_date = models.DateField()
    user_id = models.TextField(max_length=15)
    # should be related to user table will be done later
    created_at = models.DateField(auto_now_add=True)
    sales_man_id = models.TextField(max_length=15)
    # should be related to user table will be done later
    status = models.BooleanField()
    # if 0 the status will appear Blocked, if 1 the status will appear active
    active_till_date = models.DateField(blank=True, null=True)
    blocked_till_date = models.DateField(blank=True, null=True)

    # price_list_code = models.ForeignKey(PriceList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomerCategory(models.Model):
    customer_code = models.ForeignKey(Customer)
    category_code = models.ForeignKey(Category)

    def __str__(self):
        return 'Category'