from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import generics, permissions
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()
# Create your views here.

#User registration ApiView

class RegisterUserView(APIView):
#Getting data from user registration request
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

    #Data validation
        if not username or not password or not email:
            raise ValidationError('Please provide username, password and email')
        
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Username already exists', status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Email already exists', status.HTTP_400_BAD_REQUEST)
    #New user registration
        user = CustomUser.objects.create_user(username=username, password=password, email=email)

        return Response({'message':'User registered successfully'}), status.HTTP_201_CREATED
    
    #User login ApiView
class LoginUserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = CustomUser.objects.filter(username=username, password=password)

        if user:
            return Response({'message':'User logged in successfully'})

        else:
            return Response({'message':'Invalid credentials'})

class UserProfileView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        data = {
            'username': user.username,
            'email': user.email,
            'bio': user.bio,
            'profile_picture': user.profile_picture,
            'followers': user.followers.count(),
        }
       
        return Response(data)

    def put(self, request, format=None):
        user = request.user
        user.profile_picture = request.data.get('profile_picture')
        user.bio = request.data.get('bio')
        user.save()
        return Response({'message': 'Profile updated successfully'})
    
#Creating endpoints for Managing Followers
#Follow Management Views:

class FollowUserView(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    #Following user
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

#Unfollowing user
    def destroy(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)