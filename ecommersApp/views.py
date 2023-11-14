from django.shortcuts import render
from django.http import HttpResponse
from ecommersApp.models import Product, Category, Vendor, CartOrder, CartOrderItems,ProductImages,ProductReview,Address,wishlist


# Create your views here.
def index(request):
    products = Product.objects.all()
#filter(product_status="published", featured=True)
    context = {
        "products" :products
    }
    

    return render(request, 'core/base.html', context)


def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories" :categories
    }
    

    return render(request, 'core/category_list_view.html', context)


def products_list_view(request):

    products = Product.objects.all()

    context = {
        "products" :products
    }
   
    return render(request, 'core/product-list.html', context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)


    context = {
        "category":category,
        "products":products
    }
    return render(request, "core/category-product-list.html", context)

