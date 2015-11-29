# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.utils import translation

from staticgen.staticgen_pool import staticgen_pool
from staticgen.staticgen_views import StaticgenView


class StaicgenDemoStaticViews(StaticgenView):

    def items(self):
        return (
            'sitemap.xml',
            'robots.txt',
            'page_not_found',
            'server_error',
        )

staticgen_pool.register(StaicgenDemoStaticViews)


class StaticgenCMSView(StaticgenView):

    def items(self):
        try:
            from cms.models import Title
        except ImportError:  # pragma: no cover
            # django-cms is not installed.
            return super(StaticgenCMSView, self).items()

        items = Title.objects.public().filter(
            page__login_required=False,
            page__site_id=settings.SITE_ID,
        ).order_by('page__path')
        return items

    def url(self, obj):
        translation.activate(obj.language)
        url = obj.page.get_absolute_url(obj.language)
        translation.deactivate()
        return url

staticgen_pool.register(StaticgenCMSView)
