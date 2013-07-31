from django import forms
from cities.models import City


class CityForm(forms.Form):
    county_name = forms.CharField(max_length=255)

    def clean(self):
        data = self.cleaned_data.get('county_name')
        if City.objects.filter(county_name=data).exists():
            return data
        else:
            raise forms.ValidationError("Please enter a valid county name.")