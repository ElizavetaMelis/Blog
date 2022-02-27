from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
