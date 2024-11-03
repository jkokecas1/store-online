from django.shortcuts import render
from store.models import Product, ReviewRating
#from django.http import HttpResponse
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    banners = [
        'images/banners/2.jpg',
        'images/banners/3.jpg',
        'images/banners/4.jpg',
        'images/banners/5.jpg',
        'images/banners/6.jpg',
        'images/banners/7.jpg',
        'images/banners/8.jpg',
        'images/banners/9.jpg'
    ]
    # Obtener review
    for product in products:
        reviews = ReviewRating.objects.filter(product_id= product.id, status=True)
    context = {
        'products': products,
        'reviews' : reviews,
        'banners' : banners
    }
    return render(request, 'home.html', context)
    #return HttpResponse('Homepage')
