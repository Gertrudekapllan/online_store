
from django.urls import path
from .views import CategoryList, ProductList, UserProfileDetail, OrderList, OrderDetail, ProductAPIView, CategoryAPIView

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('product/', ProductAPIView.as_view(), name='product-view'),
    path('category/<int:pk>', CategoryAPIView.as_view(), name='category-view'),
    # path('category/', CategoryAPIView.as_view(), name='category-view'),
    path('user-profile/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
