from rest_framework import serializers
from .models import Post, PostView, Comment, Category, Like, BadPostWarning


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "post_count")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "media", "category", "status", "post_count", "user", "created_date", "updated_date", "slug")

class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = ("user", "created_date", "post")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "created_date", "post", "comment")

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user","post")

class BadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user","post", "comment", "created_date")


        
        
        
        