from django.shortcuts import render , redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.conf import settings

# used ajax
from django.http import JsonResponse
from django.template.loader import render_to_string

from utils.generate_code import generate_code


import stripe
import datetime
from .models import Order , OrderDetail , Cart ,CartDetail ,Coupon
from product.models import Product
from settings.models import DeliveryFee



class OrderList(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
    


def add_to_cart(request):
    quantity = request.POST['quantity']
    product = Product.objects.get(id=request.POST['product_id'])
    cart = Cart.objects.get(user=request.user,status='InProgress')
    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, product=product)
    cart_detail.quantity = int(quantity)
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()
    return redirect(f'/product/{product.slug}')


def remove_from_cart(request,id):
    cart_detail = CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect('/product/')


def remove_from_cart_checkout(request,id):
    cart_detail = CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect('/orders/checkout')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    bub_key = settings.STRIPE_API_KEY_PUBLISHABLE

    if request.method == 'POST':
        coupon = get_object_or_404(Coupon,code=request.POST['coupon_code'])  # 404

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()
            # if (coupon.start <= today_date < coupon.end ):
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = cart.cart_total() * coupon.discount/100
                cart_total = cart.cart_total() - coupon_value
                coupon.quantity -= 1 
                coupon.save()

                cart.coupon = coupon
                cart.total_After_coupon = cart_total
                cart.save()

                total = delivery_fee + cart_total 


                cart = Cart.objects.get(user=request.user,status='InProgress')

                # coupon with ajax
                html = render_to_string('include/checkout_table.html',{
                    'cart_detail':cart_detail,
                    'sub_total':cart_total,
                    'cart_total':total,
                    'coupon':coupon_value,
                    'delivery_fee':delivery_fee,
                    'bub_key':bub_key,
                })
                return JsonResponse({'result':html})


                # return render(request,'orders/checkout.html',{
                #     'cart_detail':cart_detail,
                #     'sub_total':cart_total,
                #     'cart_total':total,
                #     'coupon':coupon_value,
                #     'delivery_fee':delivery_fee,
                # })
        
        # else:
        #     sub_total = cart.cart_total
        #     total = delivery_fee + cart.cart_total()
        #     coupon = 0


    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail,
        'sub_total':cart.cart_total,
        'cart_total':delivery_fee + cart.cart_total(),
        'coupon':0,
        'delivery_fee':delivery_fee,
        'bub_key':bub_key,
    })


def process_payment(request):
    cart = Cart.objects.get(user=request.user,status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee

    if cart.total_after_coupon:
        total = cart.total_after_coupon + delivery_fee

    else:
        total = cart.cart_total() + delivery_fee

    code = generate_code()

    stripe.api_key = settings.STRIPE_API_KEY_SECRET



    items = [
        {
            'price_data' : {
                'currency': 'usd',
                'product_data': {
                'name': code,
                },
                'unit_amount': int(total*100),
            },
        'quantity': 1,
        }
    ]

    checkout_session = stripe.checkout.Session.create(
        line_items=items,
        mode='payment',
        success_url="http://127.0.01:8000/orders/checkout/payment/success",
        cancel_url="http://127.0.01:8000/orders/checkout/payment/faild"
    )



    return JsonResponse({'session':checkout_session})



def payment_success(request):
    return redirect(request,'orders/success.html',{})




def payment_failed(request):
    return redirect(request,'orders/failed.html',{})