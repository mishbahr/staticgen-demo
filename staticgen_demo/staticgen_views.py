# -*- coding: utf-8 -*-

from __future__ import unicode_literals

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
