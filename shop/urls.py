from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *
router = DefaultRouter()
router.register(r'product', ProductViewSet)
urlpatterns = [
    #     path('categories/', CategoryList.as_view(), name='category-list'),
    #     path('products/', ProductList.as_view(), name='product-list'),
    #     path('product/', ProductAPIList.as_view(), name='product-view'),
    #     path('product/list/<int:pk>', ProductAPIList.as_view(), name='product-view'),  # list
    path('product/list/<int:pk>', ProductViewSet.as_view({'put': 'update'}), name='product-view'),
    path('product/', ProductViewSet.as_view({'get': 'list'}), name='product-view'),
    #     path('product/<int:pk>', ProductAPIUpdate.as_view(), name='product-view'),
    #     path('category/<int:pk>', CategoryAPIView.as_view(), name='category-view'),
    #     path('productdetail/<int:pk>', ProductAPIDetailView.as_view(), name='product-detail'),
    #     # path('category/', CategoryAPIView.as_view(), name='category-view'),
    #     path('user-profile/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),
    #     path('orders/', OrderList.as_view(), name='order-list'),
    #     path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
