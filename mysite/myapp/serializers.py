# myapp\serializers.py
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Book
from authors.serializers import AuthorSerializer
from authors.models import Author
from django.utils.dateparse import parse_date


class BookSerializer(serializers.ModelSerializer):
    my_sale_price = serializers.SerializerMethodField(
        read_only=True)  # Define serializer field for sale_price
    author = AuthorSerializer()
    edit_url = serializers.SerializerMethodField(read_only=True)

    # email = serializers.EmailField(write_only=True)

    class Meta:
        model = Book
        fields = ['pk', 'edit_url',
                  'title',
                  'my_sale_price',
                  'author',
                  'content',
                  'price',
                  # 'email'
                  ]

    #
    def create(self, validated_data):
        # Extract nested author data
        print("hello from create in serializer")
        print(validated_data)
        author_data = validated_data.pop('author')
        author_name = author_data.get('name')[:-2]
        print(author_name," after trim")
        author_instance, created = Author.objects.get_or_create(name=author_name, defaults=author_data)
        # Create book instance with the created author instance
        book_instance = Book.objects.create(author=author_instance,
                                            **validated_data)
        return book_instance

    def update(self, instance, validated_data):
        # Update author data if provided
        author_data = validated_data.pop('author', None)
        print(author_data)
        if author_data:
            author_name = author_data.get('name')
            birth_date = author_data.get('birth_date')
            if author_name:
                author_instance, created = Author.objects.get_or_create(name=author_name, defaults={
                    'birth_date': birth_date})
                instance.author = author_instance
            elif birth_date:
                if type(birth_date) == str:
                    instance.author.birth_date = parse_date(birth_date)
                else:
                    instance.author.birth_date = birth_date
                instance.author.save()

        # Update book instance fields
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        else:
            return reverse("book-update", kwargs={"pk": obj.pk}, request=request)

    def get_my_sale_price(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_sale_price
        else:
            return None
