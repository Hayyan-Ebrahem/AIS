from django.db import models
from django.db.models import Q
import datetime
from django.utils import six
from pandas import DataFrame
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager
from django_pandas.io import read_frame

class PandasQuerySet(QuerySet):

    def __init__(self,*args,**kwargs):
        super(PandasQuerySet,self).__init__(*args,**kwargs)
    
    def __getattr__(self, attr):
        if attr in dir(self.df):
            return getattr(self.df, attr)
        else:
            raise AttributeError("%r object has no attribute %r" %(self.__class__, attr))

    def __getitem__(self, k):
        if not isinstance(k, (slice,) + six.integer_types):
            return self.df[k]
        else:
            return super(PandasQuerySet,self).__getitem__(k)

    def test(self):
        return 'ddddddddddd'

    @property
    def df(self):
        return DataFrame(list(self.values()))

class PandasDataFrameManager(BaseManager.from_queryset(DataFrame)):

    _queryset_class = PandasQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        return self._queryset_class(**kwargs)

