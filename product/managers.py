from django.db import models
from django.db.models import Q
import datetime
from pandas import DataFrame
from django.db.models.query import QuerySet


from django.db.models.manager import BaseManager


class ProductManager(models.Manager):

    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def __init__(self, *args, **kwargs):
        print ('#############class ProductManager self is: ', type(self))
        super(ProductManager, self).__init__(*args, **kwargs)
        # Cache shared by all the get_for_* methods to speed up
        # ContentType retrieval.
        self._cache = {}

# class PandasQuerySet(QuerySet):

#     def get_queryset(self):
#     	return self.values_list()

# class PandasManager(BaseManager.from_queryset(PandasQuerySet)):
# 	print('PandasManager PandasQuerySet is:', PandasQuerySet())
# 	queryset_class = PandasQuerySet()


# class PandasManagerConcrete(PandasManager,models.Manager):
# 	pass