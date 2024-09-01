from django.urls import path, include
from .views import BookListAPIView, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    path('books/', BookListAPIView.as_view(), name = 'book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]