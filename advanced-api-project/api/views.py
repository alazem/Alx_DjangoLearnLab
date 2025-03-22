from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# Custom Create View with Validation
class CreateView(generics.CreateAPIView): 
    """
    API endpoint to create a new book.
    - Authentication required.
    - Ensures unique book titles.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Additional validation: Ensure title is unique
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            return Response({"error": "A book with this title already exists."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()  # Save the book if valid

# Custom Update View with Validation and Error Handling
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Ensure unique title constraint during updates
            title = serializer.validated_data.get('title', instance.title)
            if Book.objects.exclude(pk=instance.pk).filter(title=title).exists():
                return Response({"error": "A book with this title already exists."}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Custom List View with Filtering
class ListView(generics.ListAPIView):
    
    """
    API endpoint to list all books.
    - No authentication required.
    - Supports searching by title.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # Allows filtering books by title

# Custom Retrieve View
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

# Custom Delete View (Only Authenticated Users)
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete
    lookup_field = 'pk'
