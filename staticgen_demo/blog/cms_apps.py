# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BlogApp(CMSApp):
    name = _('Blog')
    urls = ['staticgen_demo.blog.urls']
    app_name = 'blog'

apphook_pool.register(BlogApp)
