from django.db import models
from django.db.models import Q
import datetime
from pandas import DataFrame
from django.db.models.query import QuerySet, ModelIterable
from django.db.models.manager import BaseManager
from django_pandas.io import read_frame


class ProductManager(models.Manager):

    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class DataFrameQuerySet(DataFrame, QuerySet):

    def __init__(self):
    	self.me = 'kkk'
    	self._model = None
    	self._using = None
    	self._hints = None
    def get_queryset(self):
        """
        Returns a new QuerySet object.  Subclasses can override this method to
        easily customize the behavior of the Manager.
        """
        print('The proplem is here get_queryset() on baseManager self is :', self, 'self.model:',self.model\
            ,'self.using',self.using)
        return self._queryset_class(model=self.model, using=self._db, hints=self._hints)

    _queryset_class = get_queryset
class DataFrameManager(models.Manager.from_queryset(DataFrameQuerySet)):
    use_in_migrations = False

# class PandasManager(BaseManager.from_queryset(PandasQuerySet)):
# 	print('PandasManager PandasQuerySet is:', PandasQuerySet())
# 	queryset_class = PandasQuerySet()


# class PandasManagerConcrete(PandasManager,models.Manager):
# 	pass