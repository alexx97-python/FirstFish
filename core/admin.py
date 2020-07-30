from .models import Item, OrderItem, Order, BillingAddress
from django.contrib import admin

# all empty values of the field will be displayed as 'None'
admin.site.empty_value_display = '(None)'


class ItemAdmin(admin.ModelAdmin):
    # fields = ('title', ('price', 'discount_price'), 'category', 'label', 'description')
    fieldsets = (('Items', {
                    'description': 'Add or update information you need in this form',
                    'classes': ('extrapretty', 'wide'),
                    'fields': ('title', 'price', 'discount_price', 'category')}),
                 ('Additional information', {
                     'classes': ('collapse',),
                     'fields': ('label', 'description'),
            }))
    list_display = ('title', 'price', 'discount_price', 'category')
    empty_value_display = 'unknown'


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BillingAddress)

# Register your models here.
