from django.contrib.gis import serializers
from django.forms import model_to_dict
from django.http import Http404
from rest_framework import generics, request, status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


from .models import Category, Product, UserProfile, Order
from .permissions import UserPermission
from .serializers import CategorySerializer, ProductSerializer, UserProfileSerializer, OrderSerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, UserPermission,)



    # def list(self, request, *args, **kwargs):
    #     queryset = Product.objects.all()
    #     return super().list(request, *args, **kwargs)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            return Product.objects.all()[:4]
        return Product.objects.filter(pk=pk)

    # @action(methods=['get'], detail=False)
    # def category(self, request, pk=None):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})

    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserProfileViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class ProductAPIList(generics.ListAPIView):
    queryset = Product.objects.all()[:6]
    serializer_class = ProductSerializer
    permission_classes = ()


class ProductAPIUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class ProductAPIDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserProfileDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

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


# class CategoryAPIView(APIView):
#     def post(self, request):
#         new_category = Category.objects.create(
#             name=request.data['name']
#         )
#         return Response({'category': model_to_dict(new_category)})
#
#     def delete(self, request, pk):
#         c = self.get_object(pk)
#         c.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404
