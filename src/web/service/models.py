from django.db import models
from tinymce.models import HTMLField


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_image = models.ImageField(upload_to='service_icons/', blank=True, null=True)
    parent = models.ForeignKey("self", models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField()


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True)  # optional field for icon image
    order = models.IntegerField(default=0)
    background_image = models.ImageField(upload_to='hero_backgrounds/', blank=True, null=True)
    content = HTMLField()

    def __str__(self):
        return self.title


class ServiceTechnology(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service_icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

