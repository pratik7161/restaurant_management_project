from django.shortcuts import render

from .models import MenuItem
def homepage(request):
     query = request.GET.get("q","")  # Get search term from UR;
     items = MenuItem.objects.all()

     if query:
        items = [item for item in item if query.lower() in item.name.lower()]
    return render (request, "homepage.html", {
        "item": items,
        "query": query,
    })
