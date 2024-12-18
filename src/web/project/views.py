from django.views.generic import TemplateView
from django.shortcuts import render
from .models import ProjectCategory
from .models import Project
from django.shortcuts import get_object_or_404
from src.web.project.models import Project


class ProjectView(TemplateView):
    template_name = 'project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch active projects ordered by the creation date
        context['projects'] = Project.objects.filter(is_active=True).order_by('-created_at')
        return context


class ProjectDetailView(TemplateView):
    template_name = "project_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:5]
        project_id = self.kwargs.get("id")
        context["project"] = get_object_or_404(Project, id=project_id)
        return context
