from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blogs

class BlogViewSitemap(Sitemap):

    def items(self):
        return ["blogs",]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):

    def items(self):
        return Blogs.objects.all()