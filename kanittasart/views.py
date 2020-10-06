from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render (request,'frontend/home.html' {'product' : product})

def link(request):
    return render (request,'frontend/link.html')  

  



