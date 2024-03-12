# myapp/urls.py
from django.urls import path
from .views import export_books, BookListAPIView, book_delete_view, delete_all_books, BookListView, \
    BookDetailView, BookCreateView, BookUpdateView

app_name = 'myapp'
urlpatterns = [
    path('api/books/', BookListAPIView.as_view(), name='book-list-api'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('detail/<int:id>', BookDetailView.as_view(), name='book_detail'),
    path('detail/<int:id>/delete', book_delete_view, name='book_delete'),
    path('update_book/<int:id>', BookUpdateView.as_view(), name='update_book'),
    path('add_book/', BookCreateView.as_view(), name='add_book'),
    path('delete_all_books/', delete_all_books, name='delete_all_books'),
    path('export_books/', export_books, name='export_books')
]
