from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)  # Use AUTH_USER_MODEL
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    date_posted = models.DateField(auto_now_add=True)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title