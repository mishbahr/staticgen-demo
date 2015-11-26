# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Picture


class PicturePlugin(CMSPluginBase):
    model = Picture
    name = _('Picture')
    render_template = 'plugins/picture/default.html'

    fieldsets = (
        (None, {
            'fields': ('image', 'caption', )
        }),
    )


plugin_pool.register_plugin(PicturePlugin)
