from django.shortcuts import render
from rest_framework import generics
from .models import Post, PostView, Comment, Category, Like, BadPostWarning
from .serializers import CategorySerializer, CommentSerializer, PostViewSerializer, PostSerializer, LikeSerializer, BadPostSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class PostCreateListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class CommentCreateListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.kwargs["slug"]
        queryset = queryset.filter(post__slug=post_id)
        return queryset
    
class PostViewCreateListView(generics.ListCreateAPIView):
    serializer_class = PostViewSerializer
    
    def get_queryset(self):
        queryset = PostView.objects.all()
        post_id  = self.kwargs["slug"]
        queryset = queryset.filter(post__slug = post_id)
        return queryset
    
class LikeCreateListView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    
    def get_queryset(self):
        queryset = Like.objects.all()
        post_id  = self.kwargs["slug"]
        queryset = queryset.filter(post__slug = post_id)
        return queryset
    
    
class BadPostCreateListView(generics.ListCreateAPIView):
    serializer_class = BadPostSerializer
    
    def get_queryset(self):
        queryset = BadPostWarning.objects.all()
        post_id = self.kwargs["slug"]
        queryset = queryset.filter(post__slug = post_id)
        return queryset