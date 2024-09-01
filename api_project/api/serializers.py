from rest_framework import serializers
from .models import Book

#Defining the serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
