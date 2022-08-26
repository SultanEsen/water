from django.contrib import admin
from tzdata import zoneinfo

from .models import Client, Order
from core.models import Bottle


admin.site.register(Client)
# admin.site.register(Order)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['client', 'created_at', 'finished']
    list_editable = ['finished']
    fields = ['client', 'created_at', 'updated_at', 'description', 'finished']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Order, OrderAdmin)



