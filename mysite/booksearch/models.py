# booksearch/models.py
from django.db import models


class Search(models.Model):
    objects = None
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
