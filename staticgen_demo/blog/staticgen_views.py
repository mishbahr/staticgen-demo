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
        print 'status_code: %s' % response.status_code
        if not response.status_code == 200:
            pass
        else:
            context = {}
            if hasattr(response, 'context_data'):
                context = response.context_data
            elif hasattr(response, 'context'):
                context = response.context

            print context
            try:
                return context['paginator'], response.context['is_paginated']
            except KeyError:
                pass
        return None, False


class BlogPostDetailView(StaticgenView):
    i18n = True

    def items(self):
        return Post.objects.all()


staticgen_pool.register(BlogPostListView)
staticgen_pool.register(BlogPostDetailView)


