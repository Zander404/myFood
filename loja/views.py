from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def category_list(request):
    return render(request, 'category_list.html')

def product_list(request):
    return render(request, 'product_list.html')

def marca_list(request):
    return render(request, 'marca_list.html')

def size_list(request):
    return render(request, 'size_list.html')