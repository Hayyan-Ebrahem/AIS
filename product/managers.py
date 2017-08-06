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
# class SomeMixin(OtherMixin, QuerySet):
#     def __init__(self, model=None, **kwargs):
# 	    print('RRRR COOOOOOOOOL RRRRR  SELF is:',type(self))
# 	    self.model = self.model

# 	    return super(SomeMixin,self).__init__()
class PandasQuerySet(DataFrame):
    
    def __init__(self, model, using, hints):
        print('()()()()()()()()()())(()()()()()) Here it goes expected self on PandasQuerySet is QuerySet self is:', type(self))
        #super(PandasQuerySet, self).__init__()
    # # #print('__init__ self is: ', type(self))
        #print('PPP ', type(self))
        return super(PandasQuerySet, self).__init__()
        # self.model = 'Produuuuuuuuuuuuct'
        # self.using = None
        # self.hints = None


class DataFrameManagerMixin(object):
    # def read_frame(qs, fieldnames=(), index_col=None, coerce_float=False,
    #            verbose=True):
     

    #     if fieldnames:
    #         if index_col is not None and index_col not in fieldnames:
    #             # Add it to the field names if not already there
    #             fieldnames = tuple(fieldnames) + (index_col,)
    #         fields = to_fields(qs, fieldnames)
    #     # elif is_values_queryset(qs):
    #     #     if django.VERSION < (1, 9):
    #     #         if django.VERSION < (1, 8):
    #     #             annotation_field_names = qs.aggregate_names
    #     #         else:
    #     #             annotation_field_names = list(qs.query.annotation_select)

    #     #         if annotation_field_names is None:
    #     #             annotation_field_names = []

    #     #         extra_names = qs.extra_names
    #     #         if extra_names is None:
    #     #             extra_names = []

    #     #         fieldnames = qs.field_names + annotation_field_names + extra_names

    #     #         fields = [None if '__' in f else qs.model._meta.get_field(f)
    #     #                   for f in qs.field_names] + \
    #     #             [None] * (len(annotation_field_names) + len(extra_names))

        
    #         # annotation_field_names = list(qs.query.annotation_select)

    #         # select_field_names = list(qs.query.values_select)
    #         # extra_field_names = list(qs.query.extra_select)

    #         # fieldnames = select_field_names + annotation_field_names \
    #         #         + extra_field_names

    #         # fields = [None if '__' in f else qs.model._meta.get_field(f)
    #         #             for f in select_field_names] + [None] * (len(annotation_field_names) + len(extra_field_names))
    #         # else:
    #         fields = qs.model._meta.fields
    #         fieldnames = [f.name for f in fields]

    #     fieldnames = pd.unique(fieldnames)

    #     if is_values_queryset(qs):
    #         recs = list(qs)
    #     else:
    #         recs = list(qs.values_list(*fieldnames))

    #     df = pd.DataFrame.from_records(recs, columns=fieldnames,
    #                                    coerce_float=coerce_float)

    #     if verbose:
    #         update_with_verbose(df, fieldnames, fields)

    #     if index_col is not None:
    #         df.set_index(index_col, inplace=True)

    #     return df


    # def __init__(self, *args, **kwargs):
    #     print('@@@@ this is __init__ PandasManagerMixin and dir(PandasQuerySet) :', dir(PandasQuerySet),' AND self is:', type(self),'\n')

    #     super(PandasManagerMixin, self).__init__()
    _queryset_class = PandasQuerySet
    def get_queryset(self):
        """
        Return queryset limited to not removed entries.
        """
        #print('I have no idea what is this self ', self,' ')
        qs = super(DataFrameManagerMixin, self).get_queryset()
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        print('\n\n\n++++++++++++++++++++++++++++ DataFrameMixin first class inherited override get_queryset() this is the first call to get_queryset() on any Manager self is :', 
        	self,'and _queryset_class :',self._queryset_class,' \n and dir(self._queryset_class)', dir(self._queryset_class))
        #rint('@@@@ In get_queryset dir(PandasQuerySet) :', dir(PandasQuerySet))
        return self._queryset_class(**kwargs)



class DataFrameManager(DataFrameManagerMixin, models.Manager):
    pass
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











