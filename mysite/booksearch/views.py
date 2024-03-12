from django.shortcuts import render
from myapp.models import Book
from authors.models import Author
from .forms import SearchForm
from .models import Search
from django.apps import apps

model_dict = {'book': Book, 'authors:': Author}


def search_view(request, model,
                template_name='booksearch/search_results.html'):
    form = SearchForm(request.GET)
    model_class = model_dict[model]
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        # model_class = Book
        print(model_class)
        Search.objects.create(query=query)
        if model_class:
            results = model_class.objects.filter(
                searchable_text__icontains=query)

    context = {'form': form, 'results': results, 'model': model}
    return render(request, template_name, context)
