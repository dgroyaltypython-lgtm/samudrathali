from django.contrib import admin
from .models import (
    SalePaymentType,
    DailySale
)


@admin.register(SalePaymentType)
class SalePaymentTypeAdmin(admin.ModelAdmin):

    list_display = ['name']


@admin.register(DailySale)
class DailySaleAdmin(admin.ModelAdmin):

    list_display = [
        'sale_date',
        'payment_type',
        'total_amount'
    ]

    list_filter = [
        'sale_date',
        'payment_type'
    ]