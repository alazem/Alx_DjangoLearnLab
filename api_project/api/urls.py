from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list-create'),
]
