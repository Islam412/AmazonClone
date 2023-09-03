from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, queryset_depug


urlpatterns = [
    path('', ProductList.as_view()),
    path('depug',queryset_depug),
    path('<slug:slug>', ProductDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),
]