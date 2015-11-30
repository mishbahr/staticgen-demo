# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from staticgen.staticgen_pool import staticgen_pool
from staticgen.staticgen_views import StaticgenView

from .models import Post


class BlogPostListView(StaticgenView):
    is_paginated = True
    i18n = True

    def items(self):
        return ('blog:posts_list', )

    def _get_paginator(self, url):
        response = self.client.get(url)
        print response.status_code
        print response.__dict__

        if not response.status_code == 200:
            pass
        else:
            try:
                return response.context['paginator'], response.context['is_paginated']
            except KeyError:
                pass
        return None, False


class BlogPostDetailView(StaticgenView):
    i18n = True

    def items(self):
        return Post.objects.all()


staticgen_pool.register(BlogPostListView)
staticgen_pool.register(BlogPostDetailView)


