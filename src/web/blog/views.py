from django.views.generic import TemplateView, DetailView
from .models import BlogPost


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        # Get the context from the parent class (TemplateView)
        context = super().get_context_data(**kwargs)

        # Add the list of blog posts to the context
        # You might want to paginate or limit the number of posts to display for performance
        context['posts'] = BlogPost.objects.all().order_by('-date_posted')  # Order by latest post first

        return context


class BlogDetailView(DetailView):
    template_name = 'blog_details.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return BlogPost.objects.filter(pk=pk)