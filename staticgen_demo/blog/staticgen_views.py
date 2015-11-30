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


class BlogPostDetailView(StaticgenView):
    i18n = True

    def items(self):
        return Post.objects.all()


staticgen_pool.register(BlogPostListView)
staticgen_pool.register(BlogPostDetailView)


