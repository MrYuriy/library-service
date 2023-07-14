from rest_framework import serializers

from books.models import Book, BookCover


class BookSerializer(serializers.ModelSerializer):
    cover = serializers.ChoiceField(choices=BookCover.choices())
    class Meta:
        model = Book
        fielsd = (
            "title",
            "author",
            "cover",
            "inventory",
            "dayly_fee"
        )