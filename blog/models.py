from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, default="Untitled")
    slug = models.SlugField(null=False, default="")
    intro = models.TextField(null=False, default="")
    body = models.TextField(default="", null=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)