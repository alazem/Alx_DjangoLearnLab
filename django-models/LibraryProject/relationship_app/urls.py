from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/', views.list_books, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),  # Ensure trailing slash
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # Ensure trailing slash
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),  # Ensure trailing slash
]
