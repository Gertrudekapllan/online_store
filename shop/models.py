from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=id('name'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class ProductModel:
    def __init__(self, name, description, price, category_id):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'User Profile'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Order'
