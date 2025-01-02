from django import forms
from django.core.exceptions import ValidationError

class LengthForm(forms.Form):
    CHOICES: dict[str, str] = {
        "mm":"mm",
        "cm":"cm",
        "meter":"meter",
        "km":"km",
        "inches":"inches",
        "foot":"foot",
        "yard":"yard",
        "miles":"miles"
    }
    fromUnit = forms.ChoiceField(label="From Unit", widget=forms.Select ,choices=CHOICES)
    toUnit = forms.ChoiceField(label="To Unit", widget=forms.Select, choices=CHOICES)
    unitValue = forms.FloatField(label="Value", min_value=0, max_value=9999999999999 ,required=True)


class WeightForm(forms.Form):
    CHOICES: dict[str, str] = {
        "mg":"mg",
        "g":"g",
        "kg":"kg",
        "ounce":"ounce",
        "pound":"pound",        
    }

    fromUnit = forms.ChoiceField(label="From Unit", widget=forms.Select , choices=CHOICES)
    toUnit = forms.ChoiceField(label="To Unit", widget=forms.Select , choices=CHOICES)
    unitValue = forms.FloatField(label="Value", min_value=0, max_value=9999999999999, required=True)


class TemperatureForm(forms.Form):
    CHOICES: dict[str, str] = {
        "Celsius":"Celsius",
        "Fahrenheit":"Fahrenheit",
        "Kelvin":"Kelvin"
    }
    MINIMUM_TEMPERATURES = {
            "Celsius":-273.0,
            "Fahrenheit": -459.67,
            "Kelvin": 0.0
        }
    fromUnit = forms.ChoiceField(label="From Unit", widget=forms.Select , choices=CHOICES)
    toUnit = forms.ChoiceField(label="To Unit", widget=forms.Select , choices=CHOICES)
    unitValue = forms.FloatField(label="Value", max_value=9999999999999, required=True)

    def clean(self):
        value = self.cleaned_data["unitValue"]
        unit = self.cleaned_data["fromUnit"]
        if value < self.MINIMUM_TEMPERATURES[unit]:
            raise ValidationError(f"{unit}'s temperature cannot go bellow {self.MINIMUM_TEMPERATURES[unit]}")
            
        return self.cleaned_data