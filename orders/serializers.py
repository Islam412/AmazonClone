from rest_framework import serializers
from .models import Cart,CartDetail,Order,OrderDetail
from product.serializers import ProductListSerializers



class CartDetailSerializer(serializers.ModelSerializer):
    #product = ProductListSerializers()
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

