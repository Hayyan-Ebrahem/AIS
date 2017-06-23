from django.shortcuts import render
from django.http import HttpResponse
from sales.models import SalesOrder

# Create your views here.

def index(request):
	r = SalesOrder.objects.all()[1]
	return HttpResponse(r.customer)
