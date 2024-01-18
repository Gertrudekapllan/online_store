import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.encoders import JSONEncoder

from .models import Category, Product, UserProfile, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
# class ProductModel:
#     def __init__(self, name, description, price, category_id):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.category_id = category_id
#
#
# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     category_id = serializers.CharField()
#
#
# def encode():
#     model = ProductModel('fish', 'day', price=2000, category_id=4)
#     model_sr = ProductSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"fish","description":"day","price":2000.0,"category_id":"4"}')
#     data = JSONParser().parse(stream)
#     serializer = ProductSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
