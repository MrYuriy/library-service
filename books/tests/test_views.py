from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from rest_framework.test import force_authenticate
from books.models import Book
from books.serializers import BookSerializer
from books.views import BookViewSet
from decimal import Decimal
import json

class BookViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            cover='HARDCOVER',
            inventory=10,
            dayly_fee='9.99',
        )
        self.view = BookViewSet.as_view({'get': 'list', 'post': 'create', 'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
        self.url = '/books/'

    def test_book_retrieve(self):
        request = self.factory.get(f'{self.url}{self.book.id}/')
        force_authenticate(request, user=self.user)

        response = self.view(request, pk=self.book.id)
        self.assertEqual(response.status_code, 200)

        serializer = BookSerializer(instance=self.book)
        self.assertEqual(response.data, serializer.data)

    def test_book_update(self):
        data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'cover': 'HARD',
            'inventory': 5,
            'dayly_fee': '7.99',
        }
        
        request = self.factory.put(f'{self.url}{self.book.id}/', data=json.dumps(data), content_type='application/json')
        force_authenticate(request, user=self.user)

        response = self.view(request, pk=self.book.id)
        print(response.data)
        self.assertEqual(response.status_code, 200)

        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, 'Updated Book')
        self.assertEqual(updated_book.author, 'Updated Author')
        self.assertEqual(updated_book.cover, 'HARD')
        self.assertEqual(updated_book.inventory, 5)
        self.assertEqual(updated_book.dayly_fee, Decimal('7.99'))

    def test_book_delete(self):
        request = self.factory.delete(f'{self.url}{self.book.id}/')
        force_authenticate(request, user=self.user)

        response = self.view(request, pk=self.book.id)
        self.assertEqual(response.status_code, 204)

        self.assertFalse(Book.objects.filter(id=self.book.id).exists())