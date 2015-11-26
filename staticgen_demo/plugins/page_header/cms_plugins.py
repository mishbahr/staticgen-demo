# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PageHeader


class PageHeaderPlugin(CMSPluginBase):
    model = PageHeader
    name = _('Page Header')
    render_template = 'plugins/page_header/default.html'

    fieldsets = (
        (None, {
            'fields': ('heading', 'subheading', 'background_image', )
        }),
    )


plugin_pool.register_plugin(PageHeaderPlugin)
