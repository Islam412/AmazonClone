from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import Product,Brand



class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    #brand = BrandListSerializers() #return all brand data
    brand = serializers.StringRelatedField() # name 
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    #price_with_tax = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg'] :
            result = 0
            return result
        return avg['rate_avg']
    def get_review_count(self,product:Product):
        review = product.review_product.all().count()
        return review
    # def get_price_with_tax(self,product):
        #return product.price*1.5



class ProductDetailSerializers(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg'] :
            result = 0
            return result
        return avg['rate_avg']
    def get_review_count(self,product:Product):
        review = product.review_product.all().count()
        return review



class BrandDetailSerializers(serializers.ModelSerializer):
    Products = ProductListSerializers(source='product_name',many=True)
    class Meta:
        model = Brand
        fields = '__all__'