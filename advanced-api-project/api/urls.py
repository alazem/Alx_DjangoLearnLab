from .views import CustomBookList, CustomBookDetail, CustomBookCreate, CustomBookUpdate, CustomBookDelete
from django.urls import path

urlpatterns = [
    path('books/', CustomBookList.as_view(), name='book-list'),
    path('books/<int:pk>/', CustomBookDetail.as_view(), name='book-detail'),
    path('books/create/', CustomBookCreate.as_view(), name='book-create'),
    path('books/update/<int:pk>/', CustomBookUpdate.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', CustomBookDelete.as_view(), name='book-delete'),
]