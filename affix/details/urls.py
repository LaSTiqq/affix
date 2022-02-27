from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import StaticSitemap
from .views import send

app_name = 'details'

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('', send, name='home_view'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
]