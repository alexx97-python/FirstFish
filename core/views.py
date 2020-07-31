from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Item, OrderItem, Order, BillingAddress
from django.views.generic import ListView, DetailView, View, TemplateView
from django.utils import timezone
from .forms import CheckoutForm


class CheckoutView(View):

    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'core/checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                #TODO: add functionality for these fields
                #same_shipping_address = form.cleaned_data.get(
                #    'same_shipping_address')
                #save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                #TODO: add redirect to the selected payment option
                return redirect('core:checkout')
            messages.warning(self.request, 'Failed checkout')
            return redirect('core:checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have an active order!")
            return redirect('core:order-summary')


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'payment.html')


class HomeView(ListView):
    model = Item
    paginate_by = 6  # the number of items shown on the homepage
    template_name = 'core/home-page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


def get_items_by_rubric(request, category):
    object_list = Item.objects.filter(category=category)
    #TODO: solve the problem of getting tid of all categories on template
    context = {
        'object_list': object_list,
    }
    return render(request, 'core/home-page.html', context=context)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'core/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have an active order!")
            return redirect('/')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product-page.html'


def product_page(request):
    return render(request, 'core/product-page.html')


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated. ')
            return redirect('core:order-summary')
        else:
            messages.info(request, 'This item was added to your cart. ')
            order.items.add(order_item)
            return redirect('core:order-summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_data=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart. ')
        return redirect('core:order-summary')


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
                )[0]
            order.items.remove(order_item)
            messages.info(request, 'This item was removed from your cart. ')
            return redirect('core:order-summary')
        else:
            messages.info(request, 'This item was not in your cart. ')
            return redirect('core:product', slug=slug)
    else:
        messages.info(request, "You don't have an active order.")
        return redirect('core:product', slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
                )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, 'This item quantity was updated.')
                return redirect('core:order-summary')
            else:
                order.items.remove(order_item)
                return redirect('core:order-summary')
        else:
            messages.info(request, 'This item was not in your cart. ')
            return redirect('core:order-summary')
    else:
        messages.info(request, "You don't have an active order.")
        return redirect('core:order-summary')


class SalesListView(ListView):
    model = Item
    template_name = 'core/sales.html'
    paginate_by = 9
    context_object_name = 'object'

    def get_queryset(self):
        """
        :return: items that is on sales
        """
        items = Item.objects.exclude(discount_price__isnull=True)
        return items

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class FaqView(TemplateView):
    """
    This is a class that will represent a page with FAQ
    """
    template_name = 'core/FAQ.html'