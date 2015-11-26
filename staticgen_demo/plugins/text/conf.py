# -*- coding: utf-8 -*-

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

from appconf import AppConf


class TextPluginConf(AppConf):

    REDACTOR_OPTIONS = {
        'buttons': ('formatting', 'bold', 'italic', 'deleted', 'underline',
                    'unorderedlist', 'orderedlist', 'link', 'alignment', 'html', ),
        'direction': 'ltr',
        'plugins': ('bufferbuttons', ),
        'formatting': ('h1', 'h2', 'h3', 'h4', 'h5', 'p', 'blockquote',),
        'pastePlainText': True,
        'cleanOnPaste': True,
        'focusEnd': True,
    }

    class Meta:
        prefix = 'textplugin'
