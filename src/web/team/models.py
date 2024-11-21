from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)
    twitter_url = models.URLField(max_length=200, null=True, blank=True)
    facebook_url = models.URLField(max_length=200, null=True, blank=True)
    pinterest_url = models.URLField(max_length=200, null=True, blank=True)
    instagram_url = models.URLField(max_length=200, null=True, blank=True)
