
from django.urls import path, include
from rest_framework import routers

from .views import RegisterUserView, LoginUserView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view, name='register'),
    path('login/', LoginUserView.as_view, name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', UserProfileView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UserProfileView.as_view(), name='unfollow'),
]
