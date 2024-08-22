from django.urls import path
from .views import list_books, LibraryDetailView, index
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path("list_books/", list_books, name="list_books"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("", index, name="index"),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path("add_book/", views.can_add_book_view, name='can_add_book_view'),
    path("edit_book/", views.can_change_book_view, name='can_change_book_view'),
    path("can_delete_book_view/", views.can_delete_book_view, name='can_delete_book_view'),
]