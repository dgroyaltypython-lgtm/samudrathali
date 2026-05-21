from django.contrib import admin

from .models import (

    ExpenseCategory,
    PaymentMode,
    Expense

)


# =========================================
# EXPENSE CATEGORY ADMIN
# =========================================

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):

    list_display = [

        'name',
        'created_at'

    ]

    search_fields = [

        'name'

    ]

    ordering = [

        'name'

    ]


# =========================================
# PAYMENT MODE ADMIN
# =========================================

@admin.register(PaymentMode)
class PaymentModeAdmin(admin.ModelAdmin):

    list_display = [

        'name'

    ]

    search_fields = [

        'name'

    ]

    ordering = [

        'name'

    ]


# =========================================
# EXPENSE ADMIN
# =========================================

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    list_display = [

        'title',
        'category',
        'amount',
        'payment_status',
        'payment_method',
        'payment_mode',
        'expense_date',
        'paid_date'

    ]

    list_filter = [

        'category',
        'payment_status',
        'payment_method',
        'payment_mode',
        'expense_date'

    ]

    search_fields = [

        'title',
        'description'

    ]

    ordering = [

        '-expense_date'

    ]

    readonly_fields = [

        'created_at',
        'updated_at'

    ]

    fieldsets = (

        (

            'Expense Information',

            {

                'fields': (

                    'title',
                    'category',
                    'amount',
                    'expense_date',
                    'description',
                    'receipt'

                )

            }

        ),

        (

            'Payment Information',

            {

                'fields': (

                    'payment_status',
                    'payment_method',
                    'payment_mode',
                    'paid_date'

                )

            }

        ),

        (

            'System Information',

            {

                'fields': (

                    'created_at',
                    'updated_at'

                )

            }

        ),

    )