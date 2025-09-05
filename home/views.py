from django.shortcuts import render

from .models import Restaurant, MenuItem

from django.conf import settings

def homepage(request):
    restaurant = Restaurant.objects.first()
    items = MenuItem.objects.all()
    return render(request, "home.html", {"restaurant_name": restaurant_name,
    "items" : items,})
    