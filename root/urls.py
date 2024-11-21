from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from root.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT
from src.core.handlers import (
    handler404, handler500
)

urlpatterns = []

""" HANDLERS ------------------------------------------------------------------------------------------------------- """
handler404 = handler404
handler500 = handler500

""" INTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('', include('src.web.urls')),
    path('', include('src.api.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('team/', include('src.web.team.urls')),
    path('service/', include('src.web.service.urls')),
    path('project/', include('src.web.project.urls')),
    path('blog/', include('src.web.blog.urls')),

]

""" EXTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]

""" STATIC AND MEDIA FILES ----------------------------------------------------------------------------------------- """
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

""" DEVELOPMENT ONLY -------------------------------------------------------------------------------------------- """
if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
