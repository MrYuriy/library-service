from books.models import Book
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, AllowAny
from books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
