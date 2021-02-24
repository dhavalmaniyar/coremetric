from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemapIndex(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    def items(self):
        return ['index']
    def location(self, item):
        return reverse(item)