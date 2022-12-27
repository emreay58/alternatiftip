from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from blogs.views import BlogListView

urlpatterns = [
    path('', views.BlogListView.as_view(), name="blogs"),
    path('kategori/<slug:slug>', views.blogs_by_category, name="blogs_by_category"),
    path('<slug:slug>', views.blog_detail, name="blog_detail"),
    path('etiket/<slug:slug>', views.blogs_by_tag, name="blogs_by_tag"),
]
