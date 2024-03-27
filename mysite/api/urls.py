from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('books/', views.BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdateAPIView.as_view(),name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteAPIView.as_view())]

# urlpatterns = [
#     path('books/', views.book_alt_view),
#     path('books/<int:pk>/', views.book_alt_view)]
