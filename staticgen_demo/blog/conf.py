# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

from appconf import AppConf


class BlogConf(AppConf):
    DISQUS_SHORTNAME = 'django-staticgen'
    POST_IDENTIFIER = 'current_post'

    class Meta:
        prefix = 'blog'
