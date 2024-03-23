from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookMixinView.as_view()),
    path('books/<int:pk>/', views.BookMixinView.as_view()),
    path('books/<int:pk>/update/', views.BookMixinView.as_view()),
    path('books/<int:pk>/delete/', views.BookMixinView.as_view())]

# urlpatterns = [
#     path('books/', views.book_alt_view),
#     path('books/<int:pk>/', views.book_alt_view)]
