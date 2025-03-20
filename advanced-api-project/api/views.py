from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to list all books with filtering, search, and ordering capabilities.

    Filtering:
      - Filter by 'title', 'publication_year', and 'author'.
    
    Searching:
      - Enable text search on 'title' and the related 'author__name'.
    
    Ordering:
      - Allow ordering by 'title' and 'publication_year'.
    
    Permission:
      - Uses IsAuthenticatedOrReadOnly to grant read access to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Integrate filtering, searching, and ordering:
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Allow filtering on these fields:
    filterset_fields = ['title', 'publication_year', 'author']
    
    # Allow searching on title and author's name:
    search_fields = ['title', 'author__name']
    
    # Allow ordering by title and publication_year:
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a single book.
    Accessible by any user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
