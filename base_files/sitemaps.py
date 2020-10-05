from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Entry
from listings.models import Listing


class StaticViewsBlogSitemap(Sitemap):
    changefreq = 'always'
    priority = 1.0

    def items(self):
        return Entry.objects.all()


class StaticViewsListingsSitemap(Sitemap):
    changefreq = 'always'
    priority = 1.0

    def items(self):
        return Listing.objects.all()


#     def location(self, item):
#         return reverse(item)


# class StaticViewsGallerySitemap(Sitemap):
#     def items(self):
#         return ['home']
#
#     def location(self, item):
#         return reverse(item)
