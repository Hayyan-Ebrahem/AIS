from django.db import models
from django.db.models import Q
import datetime
#from .models import Product
from pandas import DataFrame
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager
from django_pandas.io import read_frame
# class DF(DataFrame):
#     def __getattr__(self,key):
#         print ('DF_____getattr____  key is :',key)
#         return super(DF,self).getattr(key)

#     def __init__(self, *args, **kwargs):
#         print (*args)
#         super(DF, self).__init__(*args, **kwargs)
#     @property
#     def _constructor(self):
#         return DF
#     @property
#     def _constructor_sliced(self):
#         return DF   

class PandasQuerySet(QuerySet):

    def __init__(self,*args,**kwargs):
        super(PandasQuerySet,self).__init__(*args,**kwargs)
        self.df = DataFrame#(list(self.model._base_manager.all().values()))
  
    def qsdf(self):
        return self.df(list(self.values()))

    def __getattr__(self,name):
        
        return self.qsdf().name

   

class PandasDataFrameManager( BaseManager.from_queryset(DataFrame)):

    _queryset_class = PandasQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        return self._queryset_class(**kwargs)

