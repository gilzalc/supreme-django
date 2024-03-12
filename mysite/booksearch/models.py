# booksearch/models.py
from django.db import models


class SearchableMixin(models.Model):
    """
    A mixin for adding searchable text to models.

    This mixin provides a `searchable_text` field and automatically generates
    the searchable text based on the `generate_searchable_text` method.

    Usage:
    1. Inherit from this mixin in your model.
    2. Implement the `generate_searchable_text` method in your model to specify
       how the searchable text should be generated.


    Note: Subclasses must implement the `generate_searchable_text` method.
    """
    searchable_text = models.TextField(blank=True, null=True)

    def generate_searchable_text(self):
        """
        To be implemented by subclasses.

        This method should return the text that will be used for searching.
        """
        raise NotImplementedError(
            "Subclasses must implement generate_searchable_text method")

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the searchable_text before saving.
        """
        self.searchable_text = self.generate_searchable_text()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Search(models.Model):
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
