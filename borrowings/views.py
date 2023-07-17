from django.shortcuts import get_list_or_404
from borrowings.serializers import BorrowingSerializer
from rest_framework import viewsets
from borrowings.models import Borrowing
from books.models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import date

class BookViewset(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        book_id = request.data.get("book_id")
        # user_id = request.user.id
        extend_return_date = request.data.get("extend_return_date")
        book = get_list_or_404(Book, id=book_id)

        if book.inventory > 0:
            borrowing = Borrowing.objects.create(
                extend_return_date = extend_return_date,
                user = request.user,
                book = book
            )
            book.inventory -= 1
            book.save()
            serializer = self.get_serializer(borrowing)
            return Response(serializer.data)

        else:
            return Response({"mrssage": "Book is out of stock"}, status=400)

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        borrowing = Borrowing.objects.get(id=pk)
        if borrowing.actual_return_date is None:
            borrowing.actual_return_date = date.today()
            borrowing.save()
            borrowing.book.inventory += 1
            borrowing.book.save()
            return Response({'message': 'Borrowing returned successfully'}, status=200)
        return Response({"message": "Borrowing already returned"}, status=400)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.GET.get("user_id")
        is_active = self.request.GET.get("is_active")

        if not self.request.user.is_staff():
            queryset = queryset.filter(user=self.request.user)

        if user_id :
            queryset = queryset.filter(user_id=user_id)

        if is_active:
            if is_active.lower() == "true":
                queryset = queryset.filter(actual_return_date__isnull=True)
            if is_active.lower() == "false":
                queryset = queryset.filter(actual_return_date__isnull=False)

        return queryset
