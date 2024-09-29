from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
    path("posts/<int:pk>/like/", PostViewSet.as_view({"post": "like"})),
    path("posts/<int:pk>/unlike/", PostViewSet.as_view({"post": "unlike"})),
]

