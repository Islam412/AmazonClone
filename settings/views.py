from django.shortcuts import render
from django.db.models import Count
from django.views.decorators.cache import cache_page
from product.models import Product , Brand , Review



# @cache_page(60 * 60 * 24)
def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_name'))
    sale_broducts = Product.objects.filter(flag='Sale')[:10]
    feature_broducts = Product.objects.filter(flag='Feature')[:6]
    new_broducts = Product.objects.filter(flag='New')[:10]
    reviews = Review.objects.all()[:5]
    return render(request,'settings/home.html',{
        'brands':brands ,
        'sale_broducts':sale_broducts ,
        'feature_broducts':feature_broducts ,
        'new_broducts':new_broducts ,
        'reviews':reviews ,
    })