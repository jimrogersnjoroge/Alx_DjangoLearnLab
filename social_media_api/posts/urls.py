from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
]

