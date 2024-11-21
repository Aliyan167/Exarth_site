from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from src.web.blog.models import BlogPost
from src.web.project.models import Project
from src.web.service.models import Service
from src.web.website.models import Testimonials
from src.web.team.models import TeamMember




class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        # Call the superclass method to initialize context
        context = super().get_context_data(**kwargs)

        # Add your custom data
        context['testimonials'] = Testimonials.objects.all()[:3]
        context['team_members'] = TeamMember.objects.all()[:3]

        return context


from django.views.generic import TemplateView
from src.web.blog.models import BlogPost
from src.web.project.models import Project
from src.web.service.models import Service
from src.web.website.models import Testimonials


class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:4]
        context['projects'] = Project.objects.all()[:5]
        context['testimonials'] = Testimonials.objects.all()[:3]
        context['blogs'] = BlogPost.objects.all()[:3]
        return context


#  class AboutView(TemplateView):
#      template_name = 'website/about.html'


class ContactView(TemplateView):
    template_name = 'website/contact.html'
