from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, queryset_depug , add_review
from .api import ProductListAPI,ProductDetailAPI,BrandListAPI,BrandDetailAPI

urlpatterns = [
    path('', ProductList.as_view()),
    path('depug',queryset_depug),
    path('<slug:slug>', ProductDetail.as_view()),
    path('<slug:slug>/add-review' , add_review),

    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),
    
    #api
    path('api/list',ProductListAPI.as_view()),
    path('api/list/<int:pk>',ProductDetailAPI.as_view()),
    
    path('brands/api/list',BrandListAPI.as_view()),
    path('brands/api/list/<int:pk>',BrandDetailAPI.as_view()),
]