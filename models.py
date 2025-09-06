form django.db import models
class Restaurant(models.Model):
    name = models.CharFeild(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.name


python manage.py makemigrations
python manage.py migrate

from yourapp.models import Restaurant
Restaurant.objects.create(name="My Reataurant", address="123 Main Street, city, country")
+
from django.db imoprt models
class Restaurant(models.Model):
    name = models.CharFeild(max_length=200)
    address = models.TextField()
    opening_hours = models.JSONField(defualt=dict)
    phone_number = models.CharFeild(max_length=20, blank=True)
    logo = models.ImageField(upload_to= 'restaurant_logos/', blank= True, null = True)
    
def __str__(self):
    return self.name

#
# data
{"Monday": "9:00 AM - 9:00 PM",
"Tuesday": "9:00AM - 9:00PM",
"Wednesday": "9:00AM" - "9:00PM",
"Thurseday": "9:00AM" - "9:00PM"
"Friday": "9:00AM" - "11:00AM",
"Saturday": "10:00AM" - "11:00AM",
"Sunday": "closed"}
+
from django.db import models
class MenuItem(models.Model):
    name = models.Charfield(max_length=100)
    description = models.TextField()
    price = models.DecimalField(maxdigits=6, decimal_places=2)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)


def __str__(self):
    return self.name
