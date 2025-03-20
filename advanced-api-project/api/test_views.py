# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()

        # Create a test author
        self.author = Author.objects.create(name="Test Author")

        # Create some test Book instances
        self.book1 = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Another Book",
            publication_year=2019,
            author=self.author
        )

    def test_list_books(self):
        """Test that the book list endpoint returns all books."""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if both books are returned in the response
        self.assertEqual(len(response.data), 2)
        titles = [book['title'] for book in response.data]
        self.assertIn("Test Book", titles)
        self.assertIn("Another Book", titles)

    def test_filter_books_by_publication_year(self):
        """Test filtering books by publication_year."""
        url = reverse('book-list') + '?publication_year=2020'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return only the book with publication_year 2020
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_search_books(self):
        """Test searching books by title and author name."""
        url = reverse('book-list') + '?search=Another'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return only the matching book
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Another Book")

    def test_ordering_books(self):
        """Test ordering books by title (ascending)."""
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # "Another Book" should come before "Test Book" alphabetically
        self.assertEqual(response.data[0]['title'], "Another Book")

    def test_book_detail(self):
        """Test retrieving the details of a single book."""
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a new book."""
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a new book."""
        self.client.login(username="testuser", password="testpassword")
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
        self.client.logout()

    def test_update_book_unauthenticated(self):
        """Test that unauthenticated users cannot update a book."""
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Title', 'publication_year': 2020, 'author': self.author.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test that authenticated users can update a book."""
        self.client.login(username="testuser", password="testpassword")
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Title', 'publication_year': 2020, 'author': self.author.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')
        self.client.logout()

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete a book."""
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete a book."""
        self.client.login(username="testuser", password="testpassword")
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the book is deleted from the database
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())
        self.client.logout()
