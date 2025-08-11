from django.shortcuts import render

# Create your views here.
from django.conf import settings

def home(request):
    restaurant_name = settings.RESTAURANT_NAME
    return render(request, "home.html", {"restaurant_name": restaurant_name})
    