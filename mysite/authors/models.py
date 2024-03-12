# authors/models.py
from _decimal import Decimal
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.db import models
from booksearch.models import SearchableMixin


class Author(SearchableMixin, models.Model):
    # objects = None
    name = models.CharField(max_length=100, blank=False, null=False)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    def generate_searchable_text(self):
        return f"{self.name}"