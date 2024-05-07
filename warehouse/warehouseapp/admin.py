from django.contrib import admin
from warehouseapp.models import Item, Warehouse

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'state', 'quantity', 'warehouse_id')
    search_fields = ('name', 'status', 'warehouse_id')

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'adress')
    search_fields = ('name', 'adress')

# class ProducerAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Item, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
