# -*- coding: utf-8 -*-

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

from appconf import AppConf


class EmbedlyOembedConf(AppConf):
    API_KEY = '422bcd76c6af47f6a71077d426a472a9'

    class Meta:
        prefix = 'embedly_oembed'
