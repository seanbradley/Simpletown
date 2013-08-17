from django import forms
from cars.models import Car


class CarForm(forms.Form):
    vsn = forms.CharField(max_length=12, label='VSN')

    def clean(self):
        data = self.cleaned_data.get('vsn')
        if Car.objects.filter(vsn=data).exists():  #add custom validation here
            return data
        else:
            raise forms.ValidationError("Please enter a valid VSN.")

    class Meta:
        model = Car