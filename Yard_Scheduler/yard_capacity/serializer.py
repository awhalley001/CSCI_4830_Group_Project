from rest_framework import serializers

from rest_framework import serializers

from home.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "birth_year"]