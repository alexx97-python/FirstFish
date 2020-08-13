from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

COLOUR_CHOICES = (
    ('BL', 'Black'),
    ('BW', 'Brown'),
    ('Gy', 'Gray'),
    ('Y', 'Yellow'),
    ('R', 'Red'),
    ('O', 'Orange'),
    ('B', 'Blue'),
    ('G', 'Grin')
)


class ItemCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Item(models.Model):
    '''
    This is model that represent our item in the shop
    '''
    title = models.CharField(max_length=100)
    price = models.FloatField()
    length = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    colour = models.CharField(max_length=2, choices=COLOUR_CHOICES, default='BL')
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(ItemCategory,
                                 on_delete=models.CASCADE, default=None)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/items', default='media/news/Camping.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

    def get_by_category_url(self):
        return reverse('core:items-by-category', kwargs={
            'category': self.category
        })


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='item',
                             on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media/items', default='media/news/Camping.jpg')


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_data = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def get_total_saved(self):
        total = 0
        for order_item in self.items.all():
            if order_item.item.discount_price:
                total += order_item.get_amount_saved()
        return total


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username