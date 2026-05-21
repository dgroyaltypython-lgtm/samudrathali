from django import forms

from .models import Expense


# =========================================
# EXPENSE FORM
# =========================================

class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = '__all__'

        widgets = {

            # =================================
            # TITLE
            # =================================

            'title': forms.TextInput(

                attrs={

                    'placeholder': 'Enter expense title'

                }

            ),

            # =================================
            # AMOUNT
            # =================================

            'amount': forms.NumberInput(

                attrs={

                    'placeholder': 'Enter amount'

                }

            ),

            # =================================
            # EXPENSE DATE
            # =================================

            'expense_date': forms.DateInput(

                attrs={

                    'type': 'date'

                }

            ),

            # =================================
            # PAID DATE
            # =================================

            'paid_date': forms.DateInput(

                attrs={

                    'type': 'date'

                }

            ),

            # =================================
            # DESCRIPTION
            # =================================

            'description': forms.Textarea(

                attrs={

                    'rows': 4,

                    'placeholder': 'Enter expense details'

                }

            ),

            # =================================
            # PAYMENT STATUS
            # =================================

            'payment_status': forms.Select(

                attrs={

                    'class': 'form-select'

                }

            ),

            # =================================
            # PAYMENT METHOD
            # =================================

            'payment_method': forms.Select(

                attrs={

                    'class': 'form-select'

                }

            ),

            # =================================
            # PAYMENT MODE
            # =================================

            'payment_mode': forms.Select(

                attrs={

                    'class': 'form-select'

                }

            ),

        }

    # =====================================
    # CUSTOM LABELS
    # =====================================

    labels = {

        'title': 'Expense Title',

        'amount': 'Expense Amount',

        'expense_date': 'Expense Date',

        'payment_status': 'Payment Status',

        'payment_method': 'Payment Method',

        'payment_mode': 'Payment Mode',

        'paid_date': 'Paid Date',

        'description': 'Description',

        'receipt': 'Upload Receipt'

    }