from django.contrib import admin
from .models import  ProjectCategory, Project, ProjectTechnology




@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('category',)
    inlines = [ProjectTechnologyInline]


@admin.register(ProjectTechnology)
class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ('project', 'technology', 'created_at', 'updated_at')
    search_fields = ('project__title', 'technology__name')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
