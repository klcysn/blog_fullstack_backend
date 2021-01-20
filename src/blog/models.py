from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
    def post_count(self):
        return self.post_set.count()
    
class Post(models.Model):
    OPTIONS = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    media = models.CharField(max_length=5000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default="Hello")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(max_length=10, choices=OPTIONS, default="draft")
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class BadPostWarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} => {self.post.title}"