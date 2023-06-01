from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class ServicesViewSitemap(Sitemap):

    def items(self):
        return ["hacamat","suluk","prp", "ozon",]

    def location(self, item):
        return reverse(item)