# myapp/forms.py
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    # Additional customization for labels if needed
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Book Title'
        self.fields['author'].label = 'Author Name'
