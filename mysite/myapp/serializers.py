# myapp\serializers.py
from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorSerializer
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    my_sale_price = serializers.SerializerMethodField(
        read_only=True)  # Define serializer field for sale_price
    author = AuthorSerializer()  # Use AuthorSerializer to include fields from the related Author model

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
        author_data = validated_data.pop('author')

        # Create author instance
        author_instance = Author.objects.create(**author_data)
        print("***************")
        # Create book instance with the created author instance
        book_instance = Book.objects.create(author=author_instance,
                                            **validated_data)
        return book_instance

    def get_my_sale_price(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_sale_price
        else:
            return None
