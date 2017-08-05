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


class PandasQuerySet(DataFrame, QuerySet):
    def __init__(self, model, using, hints):
    	super(PandasQuerySet, self).__init__()
    #print('__init__ self is: ', type(self))
    	#self.model = None
    	#self.using = None
    	#self.hints = None

class PandasManagerMixin(object):

    _queryset_class = PandasQuerySet
    # def __init__(self, *args, **kwargs):
    #     print('@@@@ this is __init__ PandasManagerMixin and dir(PandasQuerySet) :', dir(PandasQuerySet),' AND self is:', type(self),'\n')

    #     super(PandasManagerMixin, self).__init__()

    def get_queryset(self):
        """
        Return queryset limited to not removed entries.
        """
        qs = super(PandasManagerMixin, self).get_queryset()
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        print('@@@@ In get_queryset self is :', self,'and _queryset_class :',self._queryset_class,' and kwargs are:', kwargs)
        return self._queryset_class(**kwargs)
    #_queryset_class = get_queryset


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



class DataFrameManager(PandasManagerMixin, models.Manager):
    print('PandasManagerMixin.mro :',PandasManagerMixin.mro(),'\n\n')
#print('dir(DataFrameManager):', dir(DataFrameManager))

# class PandasManager(BaseManager.from_queryset(PandasQuerySet)):
# 	print('PandasManager PandasQuerySet is:', PandasQuerySet())
# 	queryset_class = PandasQuerySet()


# class PandasManagerConcrete(PandasManager,models.Manager):
# 	pass
class SoftDeletableQuerySetMixin(object):
    """
    QuerySet for SoftDeletableModel. Instead of removing instance sets
    its ``is_removed`` field to True.
    """

    def delete(self):
        """
        Soft delete objects from queryset (set their ``is_removed``
        field to True)
        """
        self.update(is_removed=True)


class SoftDeletableQuerySet(SoftDeletableQuerySetMixin, QuerySet):
    pass




class SoftDeletableManagerMixin(object):
    """
    Manager that limits the queryset by default to show only not removed
    instances of model.
    """
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        """
        Return queryset limited to not removed entries.
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_removed=False)


class SoftDeletableManager(SoftDeletableManagerMixin, models.Manager):
    pass










