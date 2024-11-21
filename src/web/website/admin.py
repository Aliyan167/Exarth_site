from django.contrib import admin
from .models import Testimonials


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'rank', 'description')
    ordering = ('-created_at',)
