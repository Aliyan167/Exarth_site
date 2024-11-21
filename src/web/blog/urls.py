from django.urls import path
from .views import BlogView,blogDetailView
app_name = "blog"

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blog-details/', blogDetailView.as_view(), name='blog-details')
]


