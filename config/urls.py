# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _
from django.views import defaults as default_views
from django.views.generic import TemplateView

from cms.sitemaps import CMSSitemap
from staticgen.sitemaps import override_sitemaps_domain

from staticgen_demo.blog.sitemaps import BlogSitemap

admin.site.site_header = _('Staticgen Demo')
admin.site.index_title = _('Dashboard')
admin.site.site_title = _('Staticgen Demo')

sitemaps = {
    'cmspages': CMSSitemap,
    'posts': BlogSitemap,
}

urlpatterns = [
    url(r'^manage/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': override_sitemaps_domain(sitemaps)}, name='sitemap.xml'),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain'), name='robots.txt'),
    url(r'^404/$', default_views.page_not_found, name='page_not_found'),
    url(r'^500/$', default_views.server_error, name='server_error'),
    url(r'^', include('cms.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
