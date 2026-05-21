from django import forms
from .models import PurchaseRequest


class PurchaseRequestForm(forms.ModelForm):

    class Meta:

        model = PurchaseRequest

        fields = '__all__'

        widgets = {

            'request_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'rows': 3
                }
            )
        }