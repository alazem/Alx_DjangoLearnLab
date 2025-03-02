from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('books/', list_books, name= 'list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name= 'library_detail'),
    path('login/', login_view, name= 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('register/', register_view, name= 'register'),
]