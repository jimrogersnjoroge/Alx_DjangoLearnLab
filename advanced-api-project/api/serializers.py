#Creating Custom Serializers

from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
#Creating a BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author'] # or fields = '__all__'

#Adding custom validation to the BookSerializer to ensure the publication_year is not in the future.
    def validate_pubclication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future')
        return value

#Creating AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    
    #A nested BookSerializer to serialize the related books dynamically.
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']