# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.sitemaps import Sitemap

from .models import Post


class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.publication_date
