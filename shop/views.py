from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, UserProfile, Order
from .serializers import CategorySerializer, ProductSerializer, UserProfileSerializer, OrderSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductAPIView(APIView):
    def get(self, request):
        lst = Product.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        return Response({'product': "RAPAPAM"})
