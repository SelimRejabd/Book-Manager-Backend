from django.urls import path
from .views import getBooks, addBook, updateBook, deleteBook

urlpatterns = [
    path('books/', getBooks, name='get_books'),
    path('books/add/', addBook, name='add_book'),
    path('books/update/<int:pk>/', updateBook, name='update_book'),
    path('books/delete/<int:pk>/', deleteBook, name='delete_book'),
]
