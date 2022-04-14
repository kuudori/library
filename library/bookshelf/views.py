from django.shortcuts import render
from rest_framework.response import Response
from .models import Author, Book
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, AuthorCreateSerializer
from rest_framework.views import APIView
from django.views.generic import View


class BookListView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class AuthorsListView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class AuthorApi(APIView):

    def put(self, request):
        serializer = AuthorCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=500)

class BookApi(APIView):

    def put(self, request):
        serializer = BookCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=500)

    def delete(self, request):
        books = Book.objects.filter(title=request.data['title'])
        books.delete()
        return Response({"Success": True}, status=201)


class BookListPage(View):
    template_name = 'bookshelf/index.html'

    def get(self, request):
        return render(request, template_name='bookshelf/index.html')
