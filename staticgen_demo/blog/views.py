# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import DetailView, ListView

from .conf import settings
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['disqus_shortname'] = settings.BLOG_DISQUS_SHORTNAME
        setattr(self.request, settings.BLOG_POST_IDENTIFIER, self.object)
        return context
