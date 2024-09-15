
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
from django_filters import rest_framework
from rest_framework import filters

class BookListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
   
#filtering using various attributes
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']

#Implementing search functionality
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

#Implementing ordering functionality
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']

#Creating a BookDetailView for retrieving a single book by ID
class BookRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class =BookSerializer



#Creating a BookCreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()   
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError(f'Book with title "{title}" already exists')
        else:
            serializer.save()

#Creating a BookUpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_update(self, data, serializer):
        if len (data['title']) == 0:
            raise serializers.ValidationError('Title cannot be empty')
        else:
            serializer.save()

    

#Creating a BookDeleteView for removing an existing book
class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_destroy(self, instance):
        instance.delete()
