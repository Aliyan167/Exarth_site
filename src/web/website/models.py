from django.db import models


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonials_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name
