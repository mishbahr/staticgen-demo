# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import EmbedlyOembed


class EmbedlyOembedPlugin(CMSPluginBase):
    model = EmbedlyOembed
    name = _('Embeds (via embed.ly)')
    render_template = 'plugins/embedly_oembed/default.html'

    fieldsets = (
        (None, {
            'fields': ('url', )
        }),
    )

plugin_pool.register_plugin(EmbedlyOembedPlugin)
