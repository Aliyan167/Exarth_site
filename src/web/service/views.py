from django.views.generic import TemplateView
from .models import Service  # Assuming you have a Service model
from django.shortcuts import get_object_or_404
from src.web.service.models import Service
from ...core.models import Technology


class ServiceView(TemplateView):
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all Service objects and order them by the 'order' field
        context['services'] = Service.objects.order_by('order')
        # Fetch all ServiceFeature objects
        return context


class ServiceDetailView(TemplateView):
    template_name = "service_details.html"

    def get_context_data(self, **kwargs):
        service = get_object_or_404(Service, id=self.kwargs['service_id'])
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:6]
        context['technology'] = Technology.objects.filter(parent__isnull=True).prefetch_related('technology_set')

        context['service'] = service
        return context
