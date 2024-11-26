from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'comments_count')  # Fields to display in the admin list view
    search_fields = ('title', 'author__username', 'content')  # Add search functionality
    list_filter = ('date_posted', 'author')  # Filters to narrow down posts
    ordering = ('-date_posted',)  # Order posts by most recent date
    prepopulated_fields = {'title': ('title',)}  # Optional: Slug field pre-population
