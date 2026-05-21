from django.contrib import admin

from .models import (
    FundCategory,
    ManagementFund,
    FundReturn
)


# =========================================
# FUND CATEGORY ADMIN
# =========================================

@admin.register(FundCategory)
class FundCategoryAdmin(admin.ModelAdmin):

    list_display = [

        'title'

    ]

    search_fields = [

        'title'

    ]


# =========================================
# MANAGEMENT FUND ADMIN
# =========================================

@admin.register(ManagementFund)
class ManagementFundAdmin(admin.ModelAdmin):

    list_display = [

        'person_name',
        'category',
        'amount',
        'total_returned',
        'pending_balance',
        'is_returnable',
        'used_date'

    ]

    list_filter = [

        'category',
        'is_returnable',
        'used_date'

    ]

    search_fields = [

        'person_name'

    ]

    ordering = [

        '-used_date'

    ]


# =========================================
# FUND RETURN ADMIN
# =========================================

@admin.register(FundReturn)
class FundReturnAdmin(admin.ModelAdmin):

    list_display = [

        'management_fund',
        'amount',
        'return_date'

    ]

    list_filter = [

        'return_date'

    ]

    ordering = [

        '-return_date'

    ]