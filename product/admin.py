from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Brand, Review

class ProductImageTabular(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','flag','price','quantity','brand']
    list_filter = ['flag','brand']
    search_fields = ['name','subtitle','descripition']
    inlines = [ProductImageTabular]



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Review)