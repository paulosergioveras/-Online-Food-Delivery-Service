from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

