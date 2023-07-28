from books.models import Book
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from books.serializers import BookSerializer
from books.permissions import IsBookAdminOrReadOnly


class BookViewSet(ModelViewSet):
    """
    Define the Book ViewSet
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsBookAdminOrReadOnly,
        ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
