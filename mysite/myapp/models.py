# myapp/models.py
from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.urls import reverse
from django.db import models


class Book(models.Model):
    # objects = None
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
        # Enforce minimum value of 0.00 on DB level
    )

    def get_absolute_url(self):
        return reverse("myapp:book_detail", kwargs={"id": self.id})
        # return f"/detail/{self.id}/"

    def __str__(self):
        return f"{self.title} Object ID: {self.id})"

    # def save(self, *args, **kwargs):
    #     # Capitalize the title before saving
    #     self.title = self.title.title()
    #     super().save(*args, **kwargs)
