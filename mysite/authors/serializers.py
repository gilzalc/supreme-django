from rest_framework import serializers
from .models import Author  # Import the Author model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']  # Include fields from the Author model
