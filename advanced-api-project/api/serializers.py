from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        if data['publication_year']>2025:
            raise serializers.ValidateError("Publication year can't be in the future")
        return data
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name', 'books']  