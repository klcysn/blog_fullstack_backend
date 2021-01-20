from rest_framework import serializers
from .models import Post, PostView, Comment, Category, Like, BadPostWarning, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "post_count")

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ("title", "content", "media", "category", "status", "postview_count",
                  "badpostwarning_count", "comment_count", "like_count", "user",
                  "created_date", "updated_date", "slug")
    def get_user(self, obj):
        return f"{obj.user.username}/{obj.user.email}"

class PostViewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    class Meta:
        model = PostView
        fields = ("user", "created_date", "post")
    def get_user(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_post(self, obj):
        return obj.post.slug

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ("user", "created_date", "post", "comment")
    def get_user(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_post(self, obj):
        return obj.post.slug


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    class Meta:
        model = Like
        fields = ("user","post")
    def get_user(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_post(self, obj):
        return obj.post.slug
class BadPostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    class Meta:
        model = BadPostWarning
        fields = ("user","post", "comment", "created_date")
    def get_user(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_post(self, obj):
        return obj.post.slug

        
        
        
        