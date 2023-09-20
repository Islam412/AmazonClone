
from .serializers import ProductListSerializers , ProductDetailSerializers , BrandDetailSerializers , BrandListSerializers
from rest_framework import generics
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


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializers


class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializers