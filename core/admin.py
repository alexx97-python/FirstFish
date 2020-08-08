from .models import Item, OrderItem, Order, BillingAddress, ItemImage, ItemCategory
from django.contrib import admin

# all empty values of the field will be displayed as 'None'
admin.site.empty_value_display = '(None)'


class ItemImageInline(admin.StackedInline):
    model = ItemImage
    extra = 3


class ItemAdmin(admin.ModelAdmin):
    # fields = ('title', ('price', 'discount_price'), 'category', 'label', 'description')
    fieldsets = (('Items', {
                    'description': 'Add or update information you need in this form',
                    'classes': ('extrapretty', 'wide'),
                    'fields': ('title', 'price', 'discount_price', 'length', 'weight', 'category', 'slug', 'image', 'colour')}),
                 ('Additional information', {
                     'classes': ('collapse',),
                     'fields': ('label', 'description'),
            }))
    list_display = ('title', 'price', 'discount_price', 'length', 'weight', 'colour')
    empty_value_display = 'unknown'
    inlines = [ItemImageInline, ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BillingAddress)
admin.site.register(ItemCategory)

# Register your models here.
