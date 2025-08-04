from django.contrib import admin
from .models import Menu,Order, OrderItem



# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1 # number of extra empty items shown by default


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','total_amount','status','created_at')
    list_filter = ('status',)
    search_fields = ('name',)
    

