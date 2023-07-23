from rest_framework import serializers
from .models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    extract = serializers.CharField(read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = '__all__'
