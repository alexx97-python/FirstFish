from django.urls import path
from .views import ItemDetailView, \
    add_to_cart, \
    remove_from_cart, \
    OrderSummaryView, \
    remove_single_item_from_cart, \
    CheckoutView, \
    PaymentView, \
    SalesListView, \
    FaqView, \
    get_items_by_rubric, \
    ContactView, \
    PaymentDeliveryView, \
    AddCouponView


app_name = 'core'

urlpatterns = [
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-single-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('sales/', SalesListView.as_view(), name='sales'),
    path('faq/', FaqView.as_view(), name='questions'),
    path('<str:category>', get_items_by_rubric, name='items-by-category'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('payment_and_delivery/', PaymentDeliveryView.as_view(), name='payment_and_delivery')

]