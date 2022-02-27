from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

from applications.post.models import Post

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comment')
    title = models.CharField(max_length=255)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='answer')
    comment = models.ForeignKey(Comment, on_delete=CASCADE, related_name='answer')
    title = models.CharField(max_length=255)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment.title

