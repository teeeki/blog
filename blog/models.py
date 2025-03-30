from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet, Count, Case, When, IntegerField



class Post(models.Model):
    title = models.CharField(max_length=255, default="Untitled")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(null=False, default="", unique=True)
    intro = models.TextField(null=False, default="")
    body = models.TextField(default="", null=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def with_state(user_id: int) -> QuerySet:
        return Articles.objects.annotate(
                likes_cnt=Count('likes'),
                liked_by_me=Case(
                    When(id__in=Likes.objects.filter(user_id=user_id).values('post_id'),
                         then=1),
                    default=0,
                    output_field=IntegerField()
                )
            )
    
    
class Like(models.Model):
    """いいね"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['post_id', 'user_id'],
                name='post_user_unique'
            )
        ]

    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)