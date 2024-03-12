# myapp/forms.py

from _decimal import Decimal
from django import forms
from django.core.validators import MinValueValidator
from .models import Book


class BookForm(forms.ModelForm):
    """
    # Overrides ModelForm fields
    Working with Django Forms: https://docs.djangoproject.com/en/5.0/topics/forms/
    """
    title = forms.CharField(max_length=100, min_length=3,
                            label='Book Title',
                            widget=forms.TextInput(attrs={
                                'placeholder': 'book title here...'})
                            )
    price = forms.DecimalField(
        validators=[MinValueValidator(Decimal('10.00'))],
        # Enforce minimum value of 0.00 on DB level
        label='Book Price',initial=10.00
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
        labels = {
            'author': 'Author Name',
        }

    # Recommendation:

    # If the customization involves simple attributes like min_length or label,
    # override the fields directly in the form. For more complex validation
    # logic, especially if it interacts with other fields,
    # centralize it in the clean_ method of the ModelForm. Here I combined those approaches.

    def clean_title(self):
        # Custom validation logic for the 'title' field
        title = self.cleaned_data['title']

        # Custom modification of the data
        modified_title = title.title()

        return modified_title

    def save(self, commit=True):
        # Override the save method to perform custom actions before saving

        # Perform additional data modification
        self.cleaned_data['title'] = self.clean_title()
        print(self.cleaned_data['price'])
        return super().save(commit)

