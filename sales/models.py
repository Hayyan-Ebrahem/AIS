from django.db import models

# Create your models here.

class SalesOrder(models.Model):
    create_date = models.DateTimeField()
    customer = models.CharField(max_length=40)
    order_number = models.IntegerField()

    def __str__(self):
        return self.customer
