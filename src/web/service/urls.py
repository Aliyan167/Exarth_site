from django.urls import path
from .views import (
    ServiceView, ServiceDetailView
)

app_name = "service"

urlpatterns = [
    path('', ServiceView.as_view(), name="service"),
    path('service-details/<int:service_id>/', ServiceDetailView.as_view(), name='service-details')

]

