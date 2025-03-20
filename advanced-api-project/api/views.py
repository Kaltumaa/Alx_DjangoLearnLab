from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books.
    Accessible by any user (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a single book by its ID.
    Accessible by any user (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Additional creation logic can be added here if needed.
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Additional update logic can be added here if needed.
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete an existing book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
