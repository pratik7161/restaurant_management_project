from django.test import TestCase

# Create your tests here.
from django.db import models
 class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)


    def __str__(self):
        return self.name



from rest_framework import serializers
from . models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name','description','price']



from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

from django.urls import path
from .views import MenuListAPIView


urlpatterns = [
    ('api/menu/', MenuListAPIView.as_view(), name='menu-list'),
    
]