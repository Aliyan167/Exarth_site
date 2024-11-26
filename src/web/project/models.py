from django.db import models
from tinymce.models import HTMLField

from src.core.models import Technology


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail_image1 = models.ImageField(upload_to='project_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, related_name='projects', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, null=True, blank=True)  # New field for location
    client = models.CharField(max_length=255, null=True, blank=True)
    content = HTMLField(default="Default Content")
    image1 = models.ImageField(upload_to='project_images/', null=True, blank=True)


def __str__(self):
    return self.title


class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, related_name='technologies', on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.title} - {self.technology.name}"
