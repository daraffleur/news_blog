from django.contrib.auth.models import User
from django.db import models
from django.db.models import PositiveIntegerField


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.content


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    link = models.URLField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    votes = PositiveIntegerField(default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
