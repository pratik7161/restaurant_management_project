import requests 
from django.shortcuts import render
def homepage(request):
    api_url = 'http://localhost:8000/api/menu'

    try:
        response = requests.get(api_url)
        menu_items = response.json() if response.status_code == 200 else[]

    except requests.exceptions.RequestException:
        menu_items = []


    return render(request, 'homepage.html',{'menu_items': menu_items})




    # for templates/homepage.html

    <!DOCTYPY HTML>
    <>