from django.contrib import admin
from .models import Category, Post, PostView, Comment, Like, BadPostWarning

admin.site.register(Category)
admin.site.register(PostView)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(BadPostWarning)
# Register your models here.
