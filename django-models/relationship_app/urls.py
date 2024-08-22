# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
# register modules
from django.contrib.auth.views import LoginView, LogoutView

from .views import   user_register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    #login and logout ,register url
     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', user_register, name='register'),

]
