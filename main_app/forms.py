from django import forms
from .models import Release


class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ['date', 'store', 'price', 'brand']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
