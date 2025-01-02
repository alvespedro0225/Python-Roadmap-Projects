from django.shortcuts import render, redirect
from django.views import View

import numpy as np
# Create your views here.

class HomePage(View):

    def get(self, request):
        return render(request, "Units/templates/home.html")

class TemperatureView(View):
    
    def get(self, request):
        return render(request, "Units/templates/temperature.html")
    
class LenghtView(View):

    units = {
        "mm":1000,
        "cm":100,
        "inch":39.3701,
        "foot":3.32084,
        "yard":1.09361,
        "meter":1,
        "km":0.001,
        "mile":0.000621371}

    def get(self, request):
        print(request.method)
        return render(request, "Units/templates/length.html")
    
    def post(self, request):
        data = dict(request.POST.items())
        previousUnit = data["from-unit"]
        newUnit = data["to-unit"]
        try:
            previousValue = int(data["value"])
        except ValueError:
            return redirect(request.path)
        valueInMeter = np.divide(previousValue, self.units[previousUnit])
        newValue = np.multiply(valueInMeter, self.units[newUnit])
        
        ctx = {"previousValue":previousValue, "previousUnit":previousUnit, "newValue":newValue, "newUnit":newUnit }

        return render(request, "Units/templates/length.html", context=ctx)
    

    
class WeightView(View):

    def get(self, request):
        return render(request, "Units/templates/weight.html")