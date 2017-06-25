from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
#from .managers import PersonManager


class Customer(models.Model):
	credit_limit = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

	


