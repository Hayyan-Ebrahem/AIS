from django.db import models
from django.db.models import Q
import datetime
#from .models import Product
from pandas import DataFrame
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager
from django_pandas.io import read_frame


class PandasQuerySet(DataFrame):
    # def __getattr__(self,key):
    #     print ('__getattr__', key)
    #     if isinstance(self,A):
    #         super(A,self).__getattr__(key)
    #     else:

    #         getattr(self,key)

    # def __init__(self,using,model,hints):
    #     self.using = using
    #     self.model = model
    #     self.hints = hints
    @property
    def _constructor(self):
        return PandasQuerySet
    @property
    def _constructor_sliced(self):
        return PandasQuerySet


    def to_pivot_table(self, fieldnames=(), verbose=True,
                           values=None, rows=None, cols=None,
                           aggfunc='mean', fill_value=None, margins=False,
                           dropna=True):
            
            df = self.to_dataframe(fieldnames, verbose=verbose)

            return df.pivot_table(values=values, fill_value=fill_value, index=rows,
                                  columns=cols, aggfunc=aggfunc, margins=margins,
                                  dropna=dropna)

    def to_timeseries(self, fieldnames=(), verbose=True,
                          index=None, storage='wide',
                          values=None, pivot_columns=None, freq=None,
                          coerce_float=False, rs_kwargs=None):
            
            assert index is not None, 'You must supply an index field'
            assert storage in ('wide', 'long'), 'storage must be wide or long'
            if rs_kwargs is None:
                rs_kwargs = {}

            if storage == 'wide':
                df = self.to_dataframe(fieldnames, verbose=verbose, index=index,
                                       coerce_float=True)
            else:
                df = self.to_dataframe(fieldnames, verbose=verbose,
                                       coerce_float=True)
                assert values is not None, 'You must specify a values field'
                assert pivot_columns is not None, 'You must specify pivot_columns'

                if isinstance(pivot_columns, (tuple, list)):
                    df['combined_keys'] = ''
                    for c in pivot_columns:
                        df['combined_keys'] += df[c].str.upper() + '.'

                    df['combined_keys'] += values.lower()

                    df = df.pivot(index=index,
                                  columns='combined_keys',
                                  values=values)
                else:
                    df = df.pivot(index=index,
                                  columns=pivot_columns,
                                  values=values)

            if freq is not None:
                df = df.resample(freq, **rs_kwargs)

            return df
    #@classmethod
    def to_dataframe(self, fieldnames=(), verbose=True, index=None,
                         coerce_float=False):
  
        
        return read_frame(self, fieldnames=fieldnames, verbose=verbose,
                              index_col=index, coerce_float=coerce_float)

class DataFrameManagerMixin(object):
 
    _queryset_class = PandasQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        
        return self._queryset_class()


class PandasDataFrameManager(DataFrameManagerMixin, BaseManager.from_queryset(DataFrame)):

    pass





