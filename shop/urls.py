from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CommentViewSet, ProductViewSet, add_rating, toggle_like

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('toggle_like/<int:product_id>/', toggle_like),
    path('add_rating/<int:product_id>/', add_rating),
]