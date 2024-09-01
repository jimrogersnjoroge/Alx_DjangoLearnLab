
#Using a simple view

from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
#Setting up a view that uses the serializer to retrieve and return book data.
class BookListAPIView(generics.ListAPIView):
    #implementing authentication
    authentication_classes = [TokenAuthentication]
    #ensuring only authenticated users can access the data from this view
    permission_classes = [IsAuthenticated]   
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Implementing CRUD Operations with ViewSets and Routers 
# in Django REST Framework using ViewSets
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    #authenticating users before they can perform CRUD operations
    authentication_classes = [TokenAuthentication]
   
   #ensuring only authenticated users can access the data from this view
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 

