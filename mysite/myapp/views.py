# myapp/views

import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from rest_framework import generics
from .serializers import BookSerializer


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list view
    else:
        form = BookForm()
    return render(request, 'myapp/add_book.html', {'form': form})


def delete_all_books(request):
    if request.method == 'GET':
        Book.objects.all().delete()
        return redirect('book_list')  # Redirect to the book list view
    return HttpResponse("Not available for now")
    # return render(request, 'myapp/delete_all_books.html')


def export_books(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Author'])

    books = Book.objects.all()
    for book in books:
        writer.writerow([book.title, book.author])
    return response


def welcome_view(request):
    return render(request, 'myapp/welcome.html', {'name': 'Zack'})


def book_detail_view(request):
    obj = Book.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'price': obj.price
    # }
    context = {'object': obj}
    return render(request, "myapp/detail.html", context)


# API views
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
