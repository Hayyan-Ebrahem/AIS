from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'



    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        qs = Product.analytics.all()
        df = qs.df
        #context['context_object_name'] = 'product_list'
        context['product_list'] = df.describe()
        return context

    # def get_geryset(self):
    #     return super(ProductListView, self).get_queryset()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product_details'] = self.object.categories.all()
        return context


    # def get_queryset(self):
    # 	return super(ProductDetailView,self).get_queryset()