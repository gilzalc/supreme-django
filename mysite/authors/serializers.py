from rest_framework import serializers
from .models import Author  # Import the Author model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']  # Include fields from the Author model

    def validate_name(self, value):
        """
        additional validation for the name- serializer level
        :param value:
        :return:
        """
        forbidden_name = 'Les'
        if value == forbidden_name:
            raise serializers.ValidationError(f"name {forbidden_name} is not allowed")
        print('validate_name')
        return value
