from django.shortcuts import render
from django.db.models import Count
from product.models import Product , Brand , Review
# Create your views here.



def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_name'))
    sale_broducts = Product.objects.filter(flag='Sale')[:10]
    Feature_broducts = Product.objects.filter(flag='Feature')[:6]
    new_broducts = Product.objects.filter(flag='New')[:10]
    reviews = Review.objects.all()[:5]
    return render(request,'settings/home.html',{
        'brands':brands ,
        'sale_broducts':sale_broducts ,
        'Feature_broducts':Feature_broducts ,
        'new_broducts':new_broducts ,
        'reviews':reviews ,
    })