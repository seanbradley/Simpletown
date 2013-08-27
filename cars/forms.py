import re

from django import forms
from django.core import validators

from cars.models import Car


class CarForm(forms.Form):

    vsn = forms.RegexField(regex=r'^[a-zA-Z\*]{6}[0-9\*]{6}$', error_messages = {'invalid': "Please enter a valid VSN."}, label='VSN')

    def clean(self):
        data = self.cleaned_data.get('vsn')
        if Car.objects.filter(vsn=data).exists():
            return data
        else:
            raise forms.ValidationError("That VSN does not exist.")

    class Meta:
        model = Car