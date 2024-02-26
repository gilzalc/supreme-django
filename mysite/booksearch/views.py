from django.shortcuts import render
from myapp.models import Book
from .forms import SearchForm


def search_view(request, model, template_name='booksearch/search_results.html'):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        model_class = Book
        print(model_class)

        if model_class:
            results = model_class.objects.filter(title__icontains=query)

    return render(request, template_name, {'form': form, 'results': results, 'model': model})