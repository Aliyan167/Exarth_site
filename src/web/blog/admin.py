from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('title', 'author', 'date_posted', 'comments_count')

    # Add filters for easier searching
    list_filter = ('author', 'date_posted')

    # Search functionality for title and author
    search_fields = ('title', 'author__username')

    # Customize the form for editing
    # Exclude the date_posted field from being editable in the admin form
    exclude = ('date_posted',)

    # Optionally, specify the fields or fieldsets for the form
    # This will also ensure that the 'date_posted' field isn't displayed
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'author', 'image', 'content', 'excerpt', 'comments_count')
    #     }),
    # )


# Register the BlogPost model with the BlogPostAdmin class
admin.site.register(BlogPost, BlogPostAdmin)
