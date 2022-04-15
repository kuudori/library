from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'

