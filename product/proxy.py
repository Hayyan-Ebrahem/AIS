from django.db.models.query import QuerySet
from pandas import DataFrame

from django.utils import six


class QuerySetDataFrame(QuerySet):
    def __init__(self):
        super(QuerySetDataFrame,self).__init__()
        self = DataFrame(list(self.values()))#(list(self.model._base_manager.all().values()))
        self.name = None

    
    def __getattr__(self, attr):
        print('attr:',attr,'\n')

        return getattr(self, attr)
    
    def __getitem__(self, k):
        if not isinstance(k, (slice,) + six.integer_types):
            return self.df[k]
        else:
            return super(QuerySetDataFrame,self).__getitem__(k)

    @property
    def df(self):
        return self._data_frame(list(self.values()))

    def contribute_to_class(self, model, name):
        if not self.name:
            self.name = name
        self.model = model
        setattr(model, name, ManagerDescriptor(self))



class ManagerDescriptor(object):

    def __init__(self, manager):
        self.manager = manager

    def __get__(self, instance, cls=None):
        print('In Descriptor __get__ self:',self,'cls:',self.manager.name)
        if instance is not None:
            raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)

        if cls._meta.abstract:
            raise AttributeError("Manager isn't available; %s is abstract" % (
                cls._meta.object_name,
            ))

        if cls._meta.swapped:
            raise AttributeError(
                "Manager isn't available; '%s.%s' has been swapped for '%s'" % (
                    cls._meta.app_label,
                    cls._meta.object_name,
                    cls._meta.swapped,
                )
            )
        
        return cls._meta.managers_map[self.manager.name]