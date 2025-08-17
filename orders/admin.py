from django.contrib import admin
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializer import OrderSerializer

# Register your models here.
class OrderListzView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                orders = Order.objects.filter(customer_user=request.user)

            else:
                customer_id = request.query_params.get("customer_id")
                if not customer_id:
                    return Response({"error":"Authentication required or provide customer_id"},
                    status=status.HTTP_400_BAD_REQUEST
                    )
                    orders = Order.objects.filter(customer_id=customer_id)

            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            except Order.DoesNotExist:
                return Response({"error":"no orders found"},
                status=status.HTTP_NOT_FOUND
                )


            