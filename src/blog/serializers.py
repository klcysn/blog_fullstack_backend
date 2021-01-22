from rest_framework import serializers
from .models import Post, PostView, Comment, Category, Like, BadPostWarning, User, CommentLike, BadCommentWarning


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "post_count")

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ("title", "content", "media", "category", "status", "postview_count",
                  "badpostwarning_count", "comment_count", "like_count", "user", "username",
                  "created_date", "updated_date", "slug")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"

class PostViewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    # post = serializers.SerializerMethodField()
    class Meta:
        model = PostView
        fields = ("username", "user", "created_date", "post")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    # def get_post(self, obj):
    #     return obj.post.slug

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    # slug = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ("username", "user", "created_date", "pk", "id", "post", "comment", "commentlike_count", "badcommentwarning_count")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    # def get_slug(self, obj):
    #     return obj.post.slug


class LikeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Like
        fields = ("user","post", "slug", "username", "pk")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_slug(self, obj):
        return obj.post.slug
class BadPostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    # post = serializers.SerializerMethodField()
    class Meta:
        model = BadPostWarning
        fields = ("user", "username", "post", "pk", "comment", "created_date")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    # def get_post(self, obj):
    #     return obj.post.slug        
        
class CommentLikeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    commentpk = serializers.SerializerMethodField()
    class Meta:
        model = CommentLike
        fields = ("user","username", "comment", "commentpk", "pk", "id")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_commentpk(self, obj):
        return obj.comment.pk
        
class BadCommentWarningSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    commentpk = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class Meta:
        model = BadCommentWarning
        fields = ("user", "username", "pk", "comment", "commentpk", "created_date")
    def get_username(self, obj):
        return f"{obj.user.username}/{obj.user.email}"
    def get_commentpk(self, obj):
        return obj.comment.pk  
