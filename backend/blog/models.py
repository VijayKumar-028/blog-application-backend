from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=CASCADE)
    category=models.ForeignKey(Category, on_delete=CASCADE)

class Comment(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")
