from django.urls import path
#from . import views
from .views import OrderList,checkout,add_to_cart,remove_from_cart,remove_from_cart_checkout , process_payment , payment_failed , payment_success
from .api import CartDetailCreateAPI,OrderListAPI,OrderDetailAPI,CreateOrderAPI,ApplyCouponAPI


app_name = 'orders'



urlpatterns = [
    path('' , OrderList.as_view()),
    path('checkout',checkout),
    path('checkout/payment' , process_payment),
    path('checkout/payment/success',payment_success),
    path('checkout/payment/failed',payment_failed),
    path('add_to_cart',add_to_cart , name='add_to_cart'),
    path('<int:id>/remove_from_cart',remove_from_cart),
    path('<int:id>/remove_from_cart_checkout',remove_from_cart_checkout),
    #api
    path('api/list/<str:username>',OrderListAPI.as_view()),
    path('api/list/<str:username>/create-order',CreateOrderAPI.as_view()),
    path('api/list/<str:username>/<int:pk>',OrderDetailAPI.as_view()),
    path('api/<str:username>/cart', CartDetailCreateAPI.as_view()),
    path('api/<str:username>/cart/apply-coupon', ApplyCouponAPI.as_view()),
]
