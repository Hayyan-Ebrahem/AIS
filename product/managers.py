from django.db import models
from django.db.models import Q
import datetime
#from .models import Product
from pandas import DataFrame
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager
from django_pandas.io import read_frame


# class ProductManager(models.Manager):

#     use_in_migrations = True

#     def get_by_natural_key(self, name):
#         return self.get(name=name)
# class OtherMixin(object):
# 	pass

class PandasQuerySet(DataFrame):
    
    def __init__(self, model, using, hints):
        print('()()()()()()()()()())(()()()()()) Here it goes expected self on PandasQuerySet is DataFrame ', dir(PandasQuerySet))
        super(PandasQuerySet, self).__init__()
    # # # #print('__init__ self is: ', type(self))
        #print('PPP ', type(self))
        #super(PandasQuerySet, self).__init__()
        # self.model = 'Produuuuuuuuuuuuct'
        # self.using = None
        # self.hints = None

    # def deconstruct(self):
    #     name, path, args, kwargs = super(PandasQuerySet, self).deconstruct()
        
    #     return name, path, args, kwargs

    def html(self):
        return self.html

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

    # _deny_methods = ['__getstate__', '__setstate__', '__getinitargs__',
    #                  '__getnewargs__', '__copy__', '__deepcopy__', '_db',
    #                  '__slots__']

    # def __init__(self, queryset_cls=None):
    #     self._queryset_cls = queryset_cls
    #     super(DataFrameManagerMixin, self).__init__()

    # def __getattr__(self, name):
    #     if name in self._deny_methods:
    #         raise AttributeError(name)
    #     if django.VERSION < (1, 6, 0):
    #         return getattr(self.get_query_set(), name)
    #     return getattr(self.get_queryset(), name)

 
    _queryset_class = PandasQuerySet

    def get_queryset(self):
        """
        Return queryset limited to not removed entries.
        """
        print('I have no idea what is this self ', self,' self.hints',self._hints)
        #qs = super(DataFrameManagerMixin, self).get_queryset()
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        
        #rint('@@@@ In get_queryset dir(PandasQuerySet) :', dir(PandasQuerySet))
        return self._queryset_class(**kwargs)


class PandasDataFrameManager(DataFrameManagerMixin, models.Manager.from_queryset(QuerySet)):
    use_in_migrations = True

# class DataFrameQuerySet(QuerySet):


#     def to_pivot_table(self, fieldnames=(), verbose=True,
#                        values=None, rows=None, cols=None,
#                        aggfunc='mean', fill_value=None, margins=False,
#                        dropna=True):
        
#         df = self.to_dataframe(fieldnames, verbose=verbose)

#         return df.pivot_table(values=values, fill_value=fill_value, index=rows,
#                               columns=cols, aggfunc=aggfunc, margins=margins,
#                               dropna=dropna)


#     def to_timeseries(self, fieldnames=(), verbose=True,
#                       index=None, storage='wide',
#                       values=None, pivot_columns=None, freq=None,
#                       coerce_float=False, rs_kwargs=None):
       
#         assert index is not None, 'You must supply an index field'
#         assert storage in ('wide', 'long'), 'storage must be wide or long'
#         if rs_kwargs is None:
#             rs_kwargs = {}

#         if storage == 'wide':
#             df = self.to_dataframe(fieldnames, verbose=verbose, index=index,
#                                    coerce_float=True)
#         else:
#             df = self.to_dataframe(fieldnames, verbose=verbose,
#                                    coerce_float=True)
#             assert values is not None, 'You must specify a values field'
#             assert pivot_columns is not None, 'You must specify pivot_columns'

#             if isinstance(pivot_columns, (tuple, list)):
#                 df['combined_keys'] = ''
#                 for c in pivot_columns:
#                     df['combined_keys'] += df[c].str.upper() + '.'

#                 df['combined_keys'] += values.lower()

#                 df = df.pivot(index=index,
#                               columns='combined_keys',
#                               values=values)
#             else:
#                 df = df.pivot(index=index,
#                               columns=pivot_columns,
#                               values=values)

#         if freq is not None:
#             df = df.resample(freq, **rs_kwargs)

#         return df

#     def to_dataframe(self, fieldnames=(), verbose=True, index=None,
#                      coerce_float=False):
        

#         return read_frame(self, fieldnames=fieldnames, verbose=verbose,
#                           index_col=index, coerce_float=coerce_float)



#print('dataFrameManagerMixin.mro :',DataFrameManagerMixin.mro(),'\n\n')
#print('dir(DataFrameManager):', dir(DataFrameManager))

# class PandasManager(BaseManager.from_queryset(PandasQuerySet)):
# 	print('PandasManager PandasQuerySet is:', PandasQuerySet())
# 	queryset_class = PandasQuerySet()


# class PandasManagerConcrete(PandasManager,models.Manager):
# 	pass











