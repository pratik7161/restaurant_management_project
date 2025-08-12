from django.conf import settings
from django.shortcuts import render

def homepage(request):
    context = {
        "restaurant_name": "Tasty_Bites",
        "phone": settings.RESTAURANT_PHONE
    }
    return render(request,"home.html", context)