from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class AskForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Описание')
    full_description = forms.CharField(max_length=3000, required=True, label='Подробное описание')
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='статус')
    date = forms.CharField(label='data', required=True, widget=forms.DateInput(attrs={'type':'date'}))