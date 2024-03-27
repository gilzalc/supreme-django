# authors/models.py
import datetime

from _decimal import Decimal
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.db import models
from booksearch.models import SearchableModel


class Author(SearchableModel, models.Model):
    # objects = None
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    birth_date = models.DateField(null=True,
                                  default=datetime.date.today)

    def __str__(self):
        return self.name

    @classmethod
    def search(cls, query=None):
        """
        Search for a author name
        """
        return cls.objects.filter(name__icontains=query)
