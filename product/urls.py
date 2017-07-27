from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[a-z0-9-]+?)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^category/((?P<id>[0-9]+)/$', views.CategoryList.as_view(), name='category_list')
]