from django import forms
from .models import DailySale


class DailySaleForm(forms.ModelForm):

    class Meta:

        model = DailySale

        fields = '__all__'

        widgets = {

            'sale_date': forms.DateInput(
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