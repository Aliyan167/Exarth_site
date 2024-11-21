from django.contrib import admin
from .models import ServiceCategory, Service


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active', 'thumbnail_image')
    list_filter = ('is_active', 'parent')
    search_fields = ('name',)
    prepopulated_fields = {"name": ("name",)}  # Auto-generate name from category


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'background_image')  # Removed 'is_active'
    list_filter = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)  # Sort services based on order field
    prepopulated_fields = {"title": ("title",)}  # Auto-generate title from title


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
