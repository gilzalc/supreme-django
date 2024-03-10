# myapp/models.py
from django.db import models


class Book(models.Model):
    # objects = None
    title = models.CharField(max_length=200,blank=False, null=False)
    author = models.CharField(max_length=100,blank=False, null=False)
    price = models.DecimalField(max_digits=1000, decimal_places=2)


    def __str__(self):
        return self.title


