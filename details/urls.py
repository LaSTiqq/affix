from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.urls import path
from .views import send


def sitemap(request):
    with open('sitemap.xml', 'r') as f:
        sitemap_content = f.read()
    return HttpResponse(sitemap_content, content_type='application/xml')


urlpatterns = [
    path('', send, name='home_view'),
    path('sitemap.xml', sitemap, name='sitemap'),
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt', content_type="text/plain")),
]
