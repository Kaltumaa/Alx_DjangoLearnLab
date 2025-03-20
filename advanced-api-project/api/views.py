from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books with filtering, searching, and ordering capabilities.
    
    Filtering:
      - Users can filter books by 'title', 'publication_year', and 'author' (using author name).
      
    Searching:
      - Enables text search on 'title' and 'author__name'.
      
    Ordering:
      - Users can order the results by 'title' and 'publication_year'.
      
    Permission:
      - Read operations are allowed to all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Set up filtering, searching, and ordering backends.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering by specific fields
    filterset_fields = ['title', 'publication_year', 'author']
    
    # Search on title and the related author's name.
    search_fields = ['title', 'author__name']
    
    # Allow ordering by title and publication_year.
    ordering_fields = ['title', 'publication_year']

# The other views remain the same:
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
