from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# django is a package shortcuts is a module and from that we are importing the function render

# products - > index
#URL - uniform request locator
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html' , {'products':products})


def new(request):
    return HttpResponse('New product')