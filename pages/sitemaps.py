from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import ServicesField

class PagesViewSitemap(Sitemap):

    def items(self):
        return ["index","about", "contact", "services",]

    def location(self, item):
        return reverse(item)

class ServicesSitemap(Sitemap):

    def items(self):
        return ServicesField.objects.all()