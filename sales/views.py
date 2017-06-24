from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesOrder

# Create your views here.

def index(request):
	r = SalesOrder.objects.all()
	return HttpResponse(dir(r))
