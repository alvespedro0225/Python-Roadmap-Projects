from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.forms import ValidationError
from .forms import LengthForm, WeightForm, TemperatureForm
import numpy as np

# Create your views here.


class HomePage(View):

    def get(self, request) -> HttpResponse:
        return render(request, "Units/templates/home.html")


class TemperatureView(View):

    template = "Units/templates/temperature.html"
    FAHRENHEIT_CONSTANT = np.divide(5.0, 9.0)

    def fahrenheitAndCelsius(self, value: float, unit: str) -> float:
        if unit == "Fahrenheit":
            first_mult: float = np.multiply(value, 32.0)
            first_sub: float = np.subtract(first_mult, 32.0)
            return np.multiply(self.FAHRENHEIT_CONSTANT, first_sub)

        first_mult: float = np.multiply(value, np.reciprocal(self.FAHRENHEIT_CONSTANT))
        return np.add(first_mult, 32)

    def fahrenheitAndKelvin(self, value: float, unit: str) -> float:
        if unit == "Fahrenheit":
            first_sub: float = np.subtract(value, 32)
            first_mult: float = np.multiply(
                first_sub, np.reciprocal(self.FAHRENHEIT_CONSTANT)
            )
            return np.add(first_mult, 273.15)

        first_sub: float = np.subtract(value, 273.15)
        first_mult: float = np.multiply(first_sub, self.FAHRENHEIT_CONSTANT)
        return np.add(first_mult, 32)

    def kevinAndCelsius(self, value: float, unit: str) -> float:
        return np.add(value, 273.0) if unit == "Kelvin" else np.subtract(value, 273.0)

    def get(self, request) -> HttpResponse:
        form = TemperatureForm()
        ctx: dict[str, TemperatureForm] = {"form": form}
        return render(request, self.template, context=ctx)

    def post(self, request):
        form = TemperatureForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form, "valid": False}
            return render(request, self.template, ctx)

        data = dict(request.POST.items())
        previousUnit: str = data["fromUnit"]
        newUnit: str = data["toUnit"]
        previousValue = float(data["unitValue"])

        if previousUnit != newUnit:
            match (previousUnit, newUnit):
                case ("Celsius", "Fahrenheit"):
                    newValue: float = self.fahrenheitAndCelsius(
                        previousValue, previousUnit
                    )
                case ("Celsius", "Kelvin"):
                    newValue: float = self.kevinAndCelsius(previousValue, previousUnit)
                case ("Fahrenheit", "Celsius"):
                    newValue: float = self.fahrenheitAndCelsius(
                        previousValue, previousUnit
                    )
                case ("Fahrenheit", "Kelvin"):
                    newValue: float = self.fahrenheitAndKelvin(
                        previousValue, previousUnit
                    )
                case ("Kelvin", "Celsius"):
                    newValue: float = self.kevinAndCelsius(previousValue, previousUnit)
                case ("Kelven", "Fahrenheit"):
                    newValue: float = np.reciprocal(
                        self.fahrenheitAndKelvin(previousValue, previousUnit)
                    )
                case _:
                    raise ValidationError("Unknown unit")
        else:
            newValue = previousValue

        ctx = {
            "previousValue": previousValue,
            "previousUnit": previousUnit,
            "newValue": newValue,
            "newUnit": newUnit,
            "valid": True,
        }

        return render(request, self.template, context=ctx)


class LenghtView(View):

    UNITS: dict[str, float] = {
        "mm": 1000.0,
        "cm": 100.0,
        "inch": 39.3701,
        "foot": 3.32084,
        "yard": 1.09361,
        "meter": 1.0,
        "km": 0.001,
        "miles": 0.000621371,
    }

    def get(self, request) -> HttpResponse:
        form = LengthForm()
        ctx: dict[str, LengthForm] = {"form": form}
        return render(request, "Units/templates/length.html", ctx)

    def post(self, request) -> HttpResponse:
        data = dict(request.POST.items())
        previousUnit: str = data["fromUnit"]
        newUnit: str = data["toUnit"]
        previousValue = float(data["unitValue"])
        valueInMeter: float = np.multiply(
            previousValue, np.reciprocal(self.UNITS[previousUnit])
        )
        newValue: float = np.multiply(valueInMeter, self.UNITS[newUnit])
        notationValue: str = np.format_float_scientific(newValue, 5)

        ctx: dict[str, float | str] = {
            "previousValue": previousValue,
            "previousUnit": previousUnit,
            "newValue": notationValue,
            "newUnit": newUnit,
        }

        return render(request, "Units/templates/length.html", context=ctx)


class WeightView(View):

    UNITS: dict[str, float] = {
        "mg": 1000000.0,
        "g": 1000.0,
        "kg": 1.0,
        "ounce": 35.274,
        "pound": 2.20462,
    }

    def get(self, request) -> HttpResponse:
        form = WeightForm()
        ctx: dict[str, WeightForm] = {"form": form}
        return render(request, "Units/templates/weight.html", context=ctx)

    def post(self, request) -> HttpResponse:
        data = dict(request.POST.items())
        previousUnit: str = data["fromUnit"]
        newUnit: str = data["toUnit"]
        previousValue = float(data["unitValue"])
        valueInMeter: float = np.multiply(
            previousValue, np.reciprocal(self.UNITS[previousUnit])
        )
        newValue: float = np.multiply(valueInMeter, self.UNITS[newUnit])
        notationValue: str = np.format_float_scientific(newValue, 5)

        ctx: dict[str, float | str] = {
            "previousValue": previousValue,
            "previousUnit": previousUnit,
            "newValue": notationValue,
            "newUnit": newUnit,
        }

        return render(request, "Units/templates/weight.html", context=ctx)
