from django.urls import path
from .views import item_list, \
    ItemDetailView, \
    add_to_cart, \
    remove_from_cart, \
    OrderSummaryView, \
    remove_single_item_from_cart, \
    CheckoutView, \
    PaymentView, \
    SalesListView



app_name = 'core'

urlpatterns = [
    path('item-list/', item_list, name='item-list'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-single-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment-option>/', PaymentView.as_view(), name='payment'),
    path('sales/', SalesListView.as_view(), name='sales')
]