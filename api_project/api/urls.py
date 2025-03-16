from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet 

router = DefaultRouter()
router.register(r'books_all', BookViewSet)

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api/users/', views.ListUsers.as_view(), name = 'api-token-authentication'),
    path('api/token/auth/', views.CustomAuthToken.as_view())
]


