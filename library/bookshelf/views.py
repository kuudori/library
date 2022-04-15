from django.shortcuts import render
from rest_framework.response import Response
from .models import Author, Book
from .serializers import BookSerializer,  AuthorSerializer
from rest_framework.views import APIView
from django.views.generic import View
from rest_framework import generics


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorsListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookDestroyView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListPage(View):
    template_name = 'bookshelf/index.html'

    def get(self, request):
        return render(request, template_name='bookshelf/index.html')
