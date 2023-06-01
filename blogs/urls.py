from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name="blogs"),
    path('kategori/<slug:slug>', views.blogs_by_category, name="blogs_by_category"),
    path('blogs/<slug:slug>', views.blog_detail, name="blog_detail")
]
