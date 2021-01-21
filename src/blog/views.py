from django.shortcuts import render
from rest_framework import generics
from .models import Post, PostView, Comment, Category, Like, BadPostWarning, CommentLike, BadCommentWarning
from .serializers import CategorySerializer, CommentSerializer, PostViewSerializer, PostSerializer, LikeSerializer, BadPostSerializer, CommentLikeSerializer, BadCommentWarningSerializer
from .pagination import PostPagination
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class PostCreateListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostPagination
    
class CommentCreateListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = PostPagination
    
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
    
    
class CommentLikeCreateListView(generics.ListCreateAPIView):
    serializer_class = CommentLikeSerializer
    
    def get_queryset(self):
        queryset = CommentLike.objects.all()
        comment_id  = self.kwargs["id"]
        queryset = queryset.filter(comment__id = comment_id)
        return queryset
    
class BadCommentCreateListView(generics.ListCreateAPIView):
    serializer_class = BadCommentWarningSerializer
    
    def get_queryset(self):
        queryset = BadCommentWarning.objects.all()
        comment_id = self.kwargs["id"]
        queryset = queryset.filter(comment__slug = comment_id)
        return queryset