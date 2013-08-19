import re

from django import forms
from django.core import validators

from cars.models import Car

#from django.core.validators import RegexValidatorimport re
#namespace_regex = re.compile(r'^[a-z\-]+$') alias = models.CharField( max_length = 100, unique = True, validators=[RegexValidator(regex=namespace_regex)] )

#code = forms.RegexField(regex=r'^\d{2}[-]\d{3}', max_length=6, widget=forms.TextInput(attrs=attrs_dict), label="Postal code")

#class RegexValidator([regex=None, message=None, code=None])


class CarForm(forms.Form):
    #vsn = forms.CharField(max_length=12, label='VSN')
    vsn = forms.RegexField(regex=r'^[a-zA-Z\*]{6}[0-9\*]{6}$', error_messages = {'invalid': "Please enter a valid VSN."}, label='VSN')

    def clean(self):
        data = self.cleaned_data.get('vsn')
        if Car.objects.filter(vsn=data).exists():
            return data
        else:
            raise forms.ValidationError("That VSN does not exist.")

    class Meta:
        model = Car