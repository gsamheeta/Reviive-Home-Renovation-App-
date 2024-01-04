from django import forms
from .models import RenovationPrice



class RenovationForm(forms.ModelForm):
    class Meta:
        model = RenovationPrice
        fields = ['item', 'price', 'name']


