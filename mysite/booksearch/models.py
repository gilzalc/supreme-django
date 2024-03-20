# booksearch/models.py
from django.db import models


class SearchableModel(models.Model):
    """
    Abstract base class for models that require a search functionality.

    """

    class Meta:
        abstract = True

    @classmethod
    def search(cls, query=None):
        """
        Abstract method for searching. Must be overridden by the inheriting model.

        Args:
            query (str): The search query.

        Raises:
            NotImplementedError: Subclasses must implement the 'search' method.
        """
        raise NotImplementedError(
            "Subclasses must implement the 'search' method.")


class Search(models.Model):
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
