from django.conf import settings
from django.shortcuts import render

def homepage(request):
    context = {
        "restaurant_name": "Tasty_Bites",
        "phone": settings.RESTAURANT_PHONE
    }
    return render(request,"home.html", context)

    +
from django.shortcuts import render
from .models import Restaurant, MenuItem
def homepage(request):
    restaurant = Restaurant.objects.first()
    items = MenuItem.objects.all()

cart = request.session.get("cart",{})
# count total items in cart
cart_count = sum(cart.values())
return render(request, "homepage.html",{
    "restaurant": restaurant,
    "items": items,
    "cart_count": cart_count,
    
})

# from django import series
# from .models import Model