from django.contrib import admin
from .models import (
    InventoryItem,
    PurchaseRequest
)


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'current_stock',
        'minimum_stock'
    ]


@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):

    list_display = [
        'item',
        'quantity',
        'status',
        'request_date'
    ]

    list_filter = [
        'status'
    ]