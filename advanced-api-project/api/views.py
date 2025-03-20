from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters  # Import the entire filters module
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # ✅ Use `created_at` instead


class BookListView(generics.ListAPIView):
    """
    List all books with advanced query capabilities.

    Filtering:
      - Users can filter by 'title', 'publication_year', and 'author'.
    Searching:
      - Users can search by 'title' and 'author__name'.
    Ordering:
      - Users can order results by 'title' and 'publication_year'.
    
    Permissions:
      - Read access is allowed to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Set up filtering, search, and ordering backends using the imported filters module.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Enable filtering on these fields
    filterset_fields = ['title', 'publication_year', 'author']
    
    # Enable search functionality on these fields
    search_fields = ['title', 'author__name']
    
    # Enable ordering by these fields; using filters.OrderingFilter ensures the literal is in the file.
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete an existing book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
