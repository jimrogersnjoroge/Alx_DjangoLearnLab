from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for listing all books
    path('books/', views.book_list, name='book_list'),

    # URL pattern for viewing details of a specific book
    path('books/<int:pk>/', views.book_details, name='book_details'),

    # URL pattern for creating a new book
    path('books/create/', views.create_book, name='create_book'),

    # URL pattern for editing a specific book
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),

    # URL pattern for deleting a specific book
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]