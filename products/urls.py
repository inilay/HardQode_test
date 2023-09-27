from django.urls import path, include
from .views import ProductAPIView, AllProductsAPIView, AllUserProductsAPIView


urlpatterns = [
    # 1 Задание
    path('api/v1/user_products/<int:id>/', AllUserProductsAPIView.as_view()),
    # 2 Задание
    path('api/v1/product/<int:id>/', ProductAPIView.as_view()),
    # 3 Задание
    path('api/v1/products/', AllProductsAPIView.as_view()),
]