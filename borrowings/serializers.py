from rest_framework import serializers
from borrowings.models import Borrowing
from books.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class BorrowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = "__all__"


class BorrowingDetailSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(source='user.email', read_only=True)
    book = serializers.CharField(source='book.title', read_only=True)


    class Meta:
        model = Borrowing
        fields = "__all__"
