from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'



class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product_details'] = self.object.categories.all()
        for p in context['product_details']:
        	print(p.name)

        return context