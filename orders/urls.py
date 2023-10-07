from django.urls import path
#from . import views
from .views import OrderList,checkout,add_to_cart,remove_from_cart,remove_from_cart_checkout

app_name = 'orders'

urlpatterns = [
    path('' , OrderList.as_view()),
    path('checkout',checkout),
    path('add_to_cart',add_to_cart , name='add_to_cart'),
    path('<int:id>/remove_from_cart',remove_from_cart),
    path('<int:id>/remove_from_cart_checkout',remove_from_cart_checkout),
    #path('orders/<int:id>/remove_from_cart_checkout', views.remove_from_cart_checkout, name='remove_from_cart_checkout'),
]
