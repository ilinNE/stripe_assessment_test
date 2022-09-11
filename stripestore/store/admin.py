from django.contrib import admin

from .models import Item, Tax, Order, Discount


class ItemInOrderInline(admin.TabularInline):
    model = Order.items.through
    list_display = ("item", "quantity")


class AdminOrder(admin.ModelAdmin):
    inlines = (ItemInOrderInline,)
    list_display = ("__str__", "tax", "discount")


admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(Discount)
admin.site.register(Order, AdminOrder)
