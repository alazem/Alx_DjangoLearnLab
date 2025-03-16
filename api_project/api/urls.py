from django.urls import path
from .views import BookListCreateAPIView

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')
urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
]