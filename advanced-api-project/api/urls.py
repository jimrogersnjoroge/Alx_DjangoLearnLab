
from django.urls import path, include
from .views import (
    BookListView,
    BookRetrieveView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/list/', BookListView.as_view(), name = 'book-list'),
    path('books/<int:pk>/', BookRetrieveView.as_view(), name = 'book-detail'),
    path('books/create/', BookCreateView.as_view(), name = 'book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name = 'book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name = 'book-delete'),
]

