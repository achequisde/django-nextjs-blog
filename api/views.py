from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView 

from django.shortcuts import get_object_or_404

from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer

class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.order_by('-created')[:5]
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsDetailView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def put(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorsView(APIView):
    def get(self, request):
        authors = Author.objects.order_by('name')
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
