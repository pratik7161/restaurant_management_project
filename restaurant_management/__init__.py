from django.db import models
from django.contrib.auth.models import User

#Assuming this 
class Menu(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, Decimal_places=2)


    def __str__(self):
        return self.name




class Order(models.Model):
    STATUS_CHOICES = [
           ('PENDING', 'Pending'),
           ('PROCCESSING'),('Proccessing').
           ('DELIVERED'),('Delivered'),
           ('CANCELLED'),('Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=Pending)
    created_at = models.dateTimeField(auto_now_add=True)


    def __str__(self):
        return f"order#{self.id} by {self.customer.username}"




    class OrderItem(models.Model):
        order = models.ForeignKey(Order,related_name'items', on_delete=models.CASCADE)
        menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)




        def __str__(self):
            return self.menu_item.price * self.quantity

        def __str__(self):
            return f"{self.quantity} x {self.menu_item.name}"
            

def save(self,*args, **kwargs):
    self.total_ammount = sum(item.get_item_total()for item in self.items.all())
    super().save(*args,**kwargs)