# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import TextPluginForm
from .models import Text


class TextPlugin(CMSPluginBase):
    model = Text
    name = _('Text')
    form = TextPluginForm
    render_template = 'plugins/text/default.html'

    fieldsets = (
        (None, {
            'classes': ('full-width', 'wide', ),
            'fields': ('body', )
        }),
    )


plugin_pool.register_plugin(TextPlugin)
