from django.contrib import sitemaps
from django.urls import reverse
from website.models import *


# static page
class StaticViewSitemap(sitemaps.Sitemap):
    protocol = "https"
    domain = "mjes.ir"  # 👈 دامنه مخصوص اپ مسجد
    priority = 1
    changefreq = "weekly"

    def items(self):
        return ["website:index" ,"website:live","website:report"]

    def location(self, item):
        return reverse(item)



class mediafile_Sitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return MediaFile.objects.all()

    def location(self, obj):
        return reverse("website:single_media", kwargs={"media_slug": obj.slug})

class clip_sitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return clip.objects.all()

    def location(self, obj):
        return reverse("website:clip", kwargs={"slug": obj.slug})
