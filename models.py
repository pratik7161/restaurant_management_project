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

