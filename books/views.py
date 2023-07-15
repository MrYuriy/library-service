from django.shortcuts import render
from books.models import Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    #authentication_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
