from django.contrib import admin
from .models import *
from django.contrib import messages
# Register your models here.

def ordered_to_being_processed(modeladmin, request, queryset):
        queryset.update(being_processed=True)
ordered_to_being_processed.short_description = "Update selected Order(s) to 'Being Processed' "


def ordered_to_being_delievered(modeladmin, request, queryset):
    queryset.update(being_delivered=True)
ordered_to_being_delievered.short_description = "Change Order(s) to 'Being delivered' "

def order_has_been_recieved(modeladmin, request, queryset):
    queryset.update(being_processed=False, recieved=True)
order_has_been_recieved.short_description = "Update selected Order(s) to 'Recieved' "


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)
make_refund_accepted.short_description = 'Change the Order(s) to refund granted'

class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'paystack_charge_id',
        'user',
        'amount',
        'timestamp'
        ]
    
    search_fields = [
        'user__username',
        'paystack_charge_id'
    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'item',
        'user',
        'ordered',
        'quantity'
    ]

    list_filter = [
            'item',
            'user',
            'ordered',
            'quantity'
    
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 
                    'ordered', 
                    'being_processed',
                    'being_delivered',
                    'recieved',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon',]
    list_display_links = [
                        'user',
                        'shipping_address',
                        'billing_address',
                        'payment',
                        'coupon',
    ]
    list_filter = [
                    'user', 
                    'ordered', 
                    'being_processed',
                    'being_delivered',
                    'recieved',
                    'refund_requested',
                    'refund_granted'
    ]

    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [ordered_to_being_processed,ordered_to_being_delievered,order_has_been_recieved, make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
        list_display = [
            'user',
            'street_address',
            'apartment_address',
            'country',
            'address_type',
            'default',
        ]

        list_filter = [
            'default',
            'address_type',
            'country'
        ]

        search_fields = [
            'user',
            'street_address',
            'apartment_address',
            'country',
            'state',
        ]

admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
admin.site.register(Refund)

admin.site.register(Payment, PaymentAdmin)
admin.site.register(CouponCode)
admin.site.register(Address, AddressAdmin)
admin.site.register(CarouselItem)
admin.site.register(OrderHistory)