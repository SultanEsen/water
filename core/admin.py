from django.contrib import admin

from .models import Bottle, BottlesCount


# admin.site.register(Bottle)
# admin.site.register(BottlesCount)


class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    list_display = ['maker', 'volume', 'description', 'in_stock']
    list_editable = ['in_stock']
    fields = ['maker', 'volume', 'description', 'in_stock']
    # readonly_fields = ['maker']


admin.site.register(Bottle, BottleAdmin)


class BottleCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ['bottle', 'count', 'order']
    list_editable = ['count']
    fields = ['bottle', 'count', 'order']
    # readonly_fields = ['bottle']


admin.site.register(BottlesCount, BottleCountAdmin)
