from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import *

#
# class MyCustomRouter(routers.SimpleRouter):
#     routers = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]


# router = MyCustomRouter()
router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
# router.register(r'category', CategoryViewSet)
# router.register(r'user', UserProfileViewSet)
# router.register(r'order', OrderViewSet)
# print(router.urls)
urlpatterns = [
    # # path('category/', CategoryList.as_view(), name='category-list'),
    # path('products/', ProductAPIList.as_view(), name='product-list'),
    # path('product/update/<int:pk>', ProductAPIUpdate.as_view(), name='product-update'),
    # path('product/delete/<int:pk>', ProductAPIDestroy.as_view(), name='product-delete'),
    #     path('product/', ProductAPIList.as_view(), name='product-view'),
    #     path('product/list/<int:pk>', ProductAPIList.as_view(), name='product-view'),  # list
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/',
         ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='product-detail')
    # path('product/<int:pk>', ProductViewSet.as_view({'get': 'retrieve'}), name='product-update'),
    # path('product/list', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    # path('product/delete/<int:pk>', ProductViewSet.as_view({'get': 'destroy'}), name='product-list'),
    # path('product/update/<int:pk>', ProductViewSet.as_view({'put': 'update'}), name='product-list'),
    #     path('product/<int:pk>', ProductAPIUpdate.as_view(), name='product-view'),
    #     path('category/<int:pk>', CategoryAPIView.as_view(), name='category-view'),
    #     path('productdetail/<int:pk>', ProductAPIDetailView.as_view(), name='product-detail'),
    #     # path('category/', CategoryAPIView.as_view(), name='category-view'),
    #     path('user-profile/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),
    #     path('orders/', OrderList.as_view(), name='order-list'),
    #     path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
