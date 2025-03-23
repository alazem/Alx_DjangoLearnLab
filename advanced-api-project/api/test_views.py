from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create a test book instance
        self.book = Book.objects.create(title="Test Book", author="John Doe", description="A test book.")

        # Authentication token (if using token-based authentication)
        self.client.login(username="testuser", password="testpass123")

        # API URLs
        self.book_list_url = "/api/books/"
        self.book_detail_url = f"/api/books/{self.book.id}/"

def test_get_books(self):
    response = self.client.get(self.book_list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertGreaterEqual(len(response.data), 1)

def test_get_book_detail(self):
    response = self.client.get(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data["title"], "Test Book")

def test_create_book(self):
    data = {"title": "New Book", "author": "Jane Doe", "description": "A new book description"}
    response = self.client.post(self.book_list_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)

def test_update_book(self):
    data = {"title": "Updated Book", "author": "John Doe", "description": "Updated description"}
    response = self.client.put(self.book_detail_url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book.refresh_from_db()
    self.assertEqual(self.book.title, "Updated Book")

def test_delete_book(self):
    response = self.client.delete(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Book.objects.filter(id=self.book.id).exists())
