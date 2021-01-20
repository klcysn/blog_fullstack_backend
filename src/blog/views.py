from django.shortcuts import render
from rest_framework import generics
from .models import Post, PostView, Comment, Category, Like, BadPostWarning
from .serializers import CategorySerializer, CommentSerializer, PostViewSerializer, PostSerializer, LikeSerializer, BadPostSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()