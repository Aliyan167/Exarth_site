from django.contrib import admin
from .models import Service, ServiceTechnology


# Define the inline class for ServiceTechnology
class ServiceTechnologyInline(admin.TabularInline):  # You can also use StackedInline
    model = ServiceTechnology
    extra = 1  # Number of empty forms to display in the inline section


# Customize the Service admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    inlines = [ServiceTechnologyInline]  # Attach the inline to Service


# Register ServiceTechnology separately (optional)
@admin.register(ServiceTechnology)
class ServiceTechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'created_at', 'updated_at')
