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


# class ProductModel:
#     def __init__(self, name, description, price, category_id):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.category_id = category_id


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('id', 'name', 'price', 'description', 'category', 'time_create', 'time_update')
        fields = "__all__"
    # name = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # price = serializers.FloatField()
    # category_id = serializers.CharField()
    # time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.price = validated_data.get('price', instance)
    #     instance.time_update = validated_data.get('time_update', instance)
    #     instance.save()
    #     return instance

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
