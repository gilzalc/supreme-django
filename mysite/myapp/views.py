# myapp/views
import csv
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, \
    DeleteView
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm
from .serializers import BookSerializer
from authors.models import Author


class BookCreateView(CreateView):
    form_class = BookForm
    queryset = Book.objects.all()
    template_name = 'myapp/add_book.html'
    success_url = reverse_lazy('myapp:book_list')

    def form_valid(self, form):
        author_name = form.cleaned_data['author']
        print("****")
        author, created = Author.objects.get_or_create(name=author_name)
        print(author, created, "****")
        # Set the author for the book
        form.instance.author = author
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response({'form': form, 'mode': 'Add'})


def delete_all_books(request):
    if request.method == 'POST':
        Book.objects.all().delete()
        return redirect('myapp:book_list')  # Redirect to the book list view
    return HttpResponse("Not available for now")


def export_books(request):
    if request.method == 'GET':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books.csv"'

        writer = csv.writer(response)
        writer.writerow(['Title', 'Author'])

        books = Book.objects.all()
        for book in books:
            writer.writerow([book.title, book.author])
        return response
    else:
        return 'not supported'


def welcome_view(request):
    return render(request, 'myapp/welcome.html', {'name': 'Zack'})


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'myapp/book_list.html'
    context_object_name = 'objects'


class BookDetailView(DetailView):
    template_name = 'myapp/detail.html'
    context_object_name = 'object'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)


class BookUpdateView(UpdateView):
    form_class = BookForm
    queryset = Book.objects.all()
    template_name = 'myapp/add_book.html'
    success_url = reverse_lazy('myapp:book_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_initial(self):
        # Retrieve the existing values from the model instance
        initial = super().get_initial()
        book = self.get_object()
        initial['title'] = book.title
        initial['author'] = book.author
        initial['price'] = book.price
        return initial

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response({'form': form, 'mode': 'Update'})

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)


def book_delete_view(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=id)
        book.delete()
        return redirect('myapp:book_list')  # Redirect to the book list view
    else:
        return HttpResponse("Not available for now")


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('myapp:book_list')
    def get_object(self, queryset=None):
        # Retrieve the book object to be deleted
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

    def delete(self, request, *args, **kwargs):
        # Override the delete method to perform additional actions if needed
        # For example, you can send a confirmation email before deleting
        print(666666666666666666666)
        return super().delete(request, *args, **kwargs)
