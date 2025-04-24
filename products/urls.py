# product/urls.py

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
