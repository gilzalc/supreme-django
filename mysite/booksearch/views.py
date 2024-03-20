from django.shortcuts import render
from myapp.models import Book
from authors.models import Author
from .forms import SearchForm
from .models import Search
from django.apps import apps as djangoApps


def search_view(request, model, app,
                template_name='booksearch/search_results.html'):
    form = SearchForm(request.GET)

    try:
        print(app, model)
        model_class = djangoApps.get_model(app_label=app, model_name=model)
    except LookupError:
        # Handle the case where the model is not found
        model_class = None

    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        # model_class = Book
        print(model_class)
        Search.objects.create(query=query)
        if model_class:
            results = model_class.search(query)
            # results = model_class.objects.filter(
            #     searchable_text__icontains=query)

    context = {'form': form, 'results': results, 'model': model}
    return render(request, template_name, context)