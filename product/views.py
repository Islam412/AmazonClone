from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, ProductImage, Brand, Review
from django.db.models import Q , F
from django.db.models.aggregates import Max,Min,Count,Avg,Sum
#cashe
from django.views.decorators.cache import cache_page

from.tasks import send_email


# @cache_page(60 * 1) #(sec min h)
def queryset_depug(request):
    #data = Product.objects.select_related('brand').all() #prefetch_related = many-to-many 
    #filter
    #data = Product.objects.filter(price__gt= 70) #<(__gt)
    #data = Product.objects.filter(price__gte= 70) #<=(__gte)
    #data = Product.objects.filter(price__lt= 70) #>(__lt)
    #data = Product.objects.filter(price__lte= 70) #>=(__lte)
    #data = Product.objects.filter(price__range = (65,70)) #(__range(x,y))
    
    
    #navigate relation
    #data = Product.objects.filter(brand__name='Connie Diaz')
    #data = Product.objects.filter(brand__price__gt=20) #navigate relation with (gt,lt)
    
    #filter with text
    #data = Product.objects.filter(name__contains='Johnson') #search for '....'
    #data = Product.objects.filter(name__startswith='Danielle') #search for start
    #data = Product.objects.filter(name__endswith='Novak') #search for end
    
    #filter tag
    #data = Product.objects.filter(tags__isnull=True) #search for tag
    
    
    #filter date & time
    #data = Review.objects.filter(created_at__year=2023) #search for date & time
    #data = Review.objects.filter(created_at__month=2023) #search for date & time
    
    
    #filter 2 values
    #data = Product.objects.filter(price__gt=80,quantity__lt=10) #search 2 values(and)
    '''data = Product.objects.filter(
        Q(quantity__lt=10)|
        Q(price__gt=80)
    ) #search 2 values(Q   or)'''

    '''data = Product.objects.filter(
        Q(quantity__lt=10)&
        Q(price__gt=80)
    ) #search 2 values(Q   &)'''

    ''' data = Product.objects.filter(
        Q(quantity__lt=10)|
        ~Q(price__gt=80)
    ) #search 2 values(Q   not)~~~~~~~~'''

    #data = Product.objects.filter(price=F('quantity')) #search tower == tower (f)
    
    
    #data = Product.objects.all().order_by('name')#ASC
    #data = Product.objects.order_by('name')#ASC
    #data = Product.objects.order_by('name','quantity')#ASC
    #data = Product.objects.order_by('name').reverse#DES
    
    #erorr
    #data = Product.objects.order_by('name')[0]#first
    #data = Product.objects.order_by('name')[-1]#last



    #data = Product.objects.earliest('name')#first
    #data = Product.objects.latest('name')#last
    
    
    #slice
    #data = Product.objects.all()[:10]
    #data = Product.objects.all()[10:20]
    
    #select columns
    #data = Product.objects.values('name','price')
    #data = Product.objects.values('name','price','brand__name')#dech
    #data = Product.objects.values_list('name','price','brand__name')#list
    
    
    #remove dublicate
    #data = Product.objects.all().distinct()

    #data = Product.objects.only('name','price')
    #data = Product.objects.defer(')
    
    #aggregate
    #data = Product.objects.aggregate(Sum('quantity'))
    #data = Product.objects.aggregate(Avg('price'))
    
    
    #annotate 
    #data = Product.objects.annotate(price_with_tax=F('price')*1.2) # add new tower


    data = Product.objects.get(id=100)

    send_email.delay()

    return render(request,'product/debug.html',{'data':data}) 



class ProductList(ListView):
    model = Product    #context : object_list , model_list
    paginate_by = 32   #select account product in paginate



class ProductDetail(DetailView):
    model = Product     #context : object : model
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    


class BrandList(ListView):
    model = Brand        #context : object_list , model_list
    queryset = Brand.objects.annotate(Product_count=Count('product_name'))
    paginate_by = 20


class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand = brand)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(Product_count=Count('product_name'))[0]
        return context
    

