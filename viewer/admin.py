from django.contrib import admin

from viewer.models import Item, OrderItem, Order, CheckoutAddress, Payment, Brand, Fuel, Transmission

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(CheckoutAddress)
admin.site.register(Payment)
admin.site.register(Brand)
admin.site.register(Fuel)
admin.site.register(Transmission)