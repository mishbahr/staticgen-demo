# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import PostDetailView, PostListView

urlpatterns = patterns(
    '',
    url(r'^$', PostListView.as_view(), name='posts_list'),
    url(r'^page/(?P<page>\d+)/$', PostListView.as_view(), name='posts_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        PostDetailView.as_view(), name='post_detail'),
)
