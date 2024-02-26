from django.urls import path
from .views import book_list, add_book, delete_all_books, export_books

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('delete_all_books/', delete_all_books, name='delete_all_books'),
    path('export_books/', export_books, name='export_books'),

]