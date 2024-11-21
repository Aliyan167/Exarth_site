from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'twitter_url', 'facebook_url', 'pinterest_url', 'instagram_url')
    search_fields = ('name', 'role')
    list_filter = ('role',)
