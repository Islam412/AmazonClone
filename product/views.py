from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, ProductImage, Brand, Review


class ProductList(ListView):
    model = Product    #context : object_list , model_list



class ProductDetail(DetailView):
    model = Product     #context : object : model