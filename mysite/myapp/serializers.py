# myapp\serializers.py
from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorSerializer
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    my_sale_price = serializers.SerializerMethodField(
        read_only=True)  # Define serializer field for sale_price
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title',
                  'my_sale_price',
                  'author',
                  'content',
                  'price']

    #
    def create(self, validated_data):

        # Extract nested author data
        print(validated_data)
        author_data = validated_data.pop('author')
        # Create author instance
        author_instance = Author.objects.create(**author_data)
        # Create book instance with the created author instance
        book_instance = Book.objects.create(author=author_instance,
                                            **validated_data)
        return book_instance

    def update(self, instance, validated_data):
        # Update author data if provided
        author_data = validated_data.pop('author', None)
        print(author_data)
        if author_data:
            author_instance = instance.author
            for key, value in author_data.items():
                setattr(author_instance, key, value)
            author_instance.save()
        # Update book instance fields
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def get_my_sale_price(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_sale_price
        else:
            return None