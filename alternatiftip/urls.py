"""alternatiftip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import PagesViewSitemap, ServicesSitemap
from blogs.sitemaps import BlogViewSitemap, BlogSitemap
from django.views.generic.base import TemplateView


sitemaps = {
   'pages' : PagesViewSitemap,
   'blogs' : BlogViewSitemap,
   'blog' : BlogSitemap,
   'services' : ServicesSitemap
}

urlpatterns = [
    path('', include('pages.urls')),
    path('makaleler/', include('blogs.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
