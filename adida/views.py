from django.shortcuts import render
from store.models import Product, ReviewRating
#from django.http import HttpResponse
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    banners = [
        { 'url':'static/images/banners/2.jpg', 'alt': 'First slide', 'class': 'carousel-item active'},
        { 'url':'static/images/banners/3.jpg', 'alt': 'second slide', 'class': 'carousel-item' },
        { 'url':'static/images/banners/4.jpg', 'alt': 'third slide', 'class': 'carousel-item' },
        { 'url':'static/images/banners/5.jpg', 'alt': 'fourth slide', 'class': 'carousel-item' },
        { 'url':'static/images/banners/6.jpg', 'alt': 'fifth slide', 'class': 'carousel-item' },
        { 'url':'static/images/banners/7.jpg', 'alt': 'sixth slide', 'class': 'carousel-item' },
        { 'url':'static/images/banners/8.jpg', 'alt': 'seventh slide', 'class': 'carousel-item' },
        { 'url':'static/images/banners/9.jpg', 'alt': 'eighth slide', 'class': 'carousel-item' },
    ]

    videoBaner = [
        'https://brand.assets.adidas.com/video/upload/q_auto,vc_auto,c_scale,w_0.5/video/upload/kids-fw21-disney-lionking-launch-clp-tc-carousel_egivfj.mp4',
        'https://brand.assets.adidas.com/video/upload/q_auto,vc_auto,c_scale,w_0.5/video/upload/tc_carrousel_hp_mx_adizero_jnqgyv.mp4',
        'https://brand.assets.adidas.com/image/upload/q_auto,vc_auto,c_scale,w_0.5/esMX/Images/t_carrousel_green_mondays_12_tcm217-831424.mp4',
        'https://brand.assets.adidas.com/video/upload/q_auto,vc_auto,c_scale,w_0.5/video/upload/global%20brand%20publishing/Statement/ss22-ivp-5/ss22-ivp-5-launch-tcar-m.mp4'
    ]
    # Obtener review
    for product in products:
        reviews = ReviewRating.objects.filter(product_id= product.id, status=True)
    context = {
        'products': products,
        'reviews' : reviews,
        'banners' : banners,
        'videos' : videoBaner
    }
    return render(request, 'home.html', context)
    #return HttpResponse('Homepage')
