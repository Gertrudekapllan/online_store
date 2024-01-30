from django.contrib.gis import serializers
from django.forms import model_to_dict
from django.http import Http404
from rest_framework import generics, request, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Category, Product, UserProfile, Order
from .serializers import CategorySerializer, ProductSerializer, UserProfileSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class UserProfileDetail(generics.RetrieveUpdateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#
#
# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class ProductAPIList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductAPIUpdate(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# от

# class ProductAPIView(APIView):
#     def post(self, request):
#         lst = Product.objects.all().values()
#         return Response({'posts': list(lst)})
#
#     def get(self, request):
#         p = Product.objects.all()
#         return Response({'products': ProductSerializer(p, many=True).data})
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method put not allowed'})
#         try:
#             instance = Product.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#         serializer = ProductSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response({'error': 'Method delete not allowed'})
#         product.delete()
#         return Response({'deleted': 'Method was deleted'})


class CategoryAPIView(APIView):
    def post(self, request):
        new_category = Category.objects.create(
            name=request.data['name']
        )
        return Response({'category': model_to_dict(new_category)})

    def delete(self, request, pk):
        c = self.get_object(pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
