from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from base_files.sitemaps import StaticViewsBlogSitemap, StaticViewsListingsSitemap

sitemaps = {
    'blog': StaticViewsBlogSitemap,
    'listing': StaticViewsListingsSitemap
}

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
