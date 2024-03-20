# myapp/models.py
from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.urls import reverse
from django.db import models
from booksearch.models import SearchableModel
from authors.models import Author


class Book(SearchableModel, models.Model):
    # objects = None
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))], default=33.33
        # Enforce minimum value of 0.00 on DB level
    )

    def get_absolute_url(self):
        return reverse("myapp:book_detail", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.title} Object ID: {self.id})"

    @classmethod
    def search(cls, query=None):
        """
        Get books with title with this query
        """
        return cls.objects.filter(title__icontains=query)

    @property
    def get_sale_price(self):
        float_val = float(self.price)
        return "%0.2f" % (float_val * 0.8)
