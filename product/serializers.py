from rest_framework import serializers
from django.db.models.aggregates import Avg
from taggit.serializers import TagListSerializerField , TaggitSerializer
from .models import Product,Brand,Review




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


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductDetailSerializers(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField() # name 
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    reviews = ReviewsSerializer(source='review_product',many=True)
    tags = TagListSerializerField()

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


class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializers(serializers.ModelSerializer):
    Products = ProductListSerializers(source='product_name',many=True)
    class Meta:
        model = Brand
        fields = '__all__'
        


class ProductCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','image','price']
