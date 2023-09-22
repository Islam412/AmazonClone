
from .serializers import ProductListSerializers , ProductDetailSerializers , BrandDetailSerializers , BrandListSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics
from .mypaginations import MyPaginations
from .myfilter import ProductFilter
from .models import Product , Brand


'''
@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:20] # list
    data = ProductSerializers(products,many=True,context={'request':request}).data # json
    return Response({'products':data})



@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id) # list
    data = ProductSerializers(products,context={'request':request}).data # json
    return Response({'product':data})

'''

class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle','descripition']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter
    pagination_class = MyPaginations
    permission_classes = [IsAuthenticated]



class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializers


class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializers