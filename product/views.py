from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'



    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        qs = Product.pandas.all()
        df = qs.to_dataframe()
        #context['context_object_name'] = 'product_list'
        context['product_list'] = df.describe()

        return context

    def get_geryset(self):
        print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOWWWWWWWWWWWWWWWWWWW')
        return super(ProductListView, self).get_queryset()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product_details'] = self.object.categories.all()
        return context


    def get_queryset(self):
    	print (' 1111 this should be first query ever on ProductManager as this is ProductDetailView() get_queryset and self is :',self)
    	return super(ProductDetailView,self).get_queryset()