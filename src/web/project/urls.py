from django.urls import path
from .views import (
    ProjectView, ProjectDetailView
)

app_name = "project"

urlpatterns = [
    path('', ProjectView.as_view(), name="project"),
    path('project-details/<int:id>/', ProjectDetailView.as_view(), name='project-details')
]
