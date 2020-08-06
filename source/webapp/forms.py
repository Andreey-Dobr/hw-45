from django import forms
from django.forms import widgets
from .models import STATUS_CHOICES , TYPE_CHOICES

default_status = STATUS_CHOICES[0][0]
default_type= TYPE_CHOICES[0][0]


class AskForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Описание')
    full_description = forms.CharField(max_length=3000, required=True, label='Подробное описание',widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='статус')
    type = forms.ChoiceField(choices=TYPE_CHOICES, initial=default_type, label='тип задачи')
    date = forms.CharField(label='data', required=True, widget=forms.DateInput(attrs={'type':'date'}))