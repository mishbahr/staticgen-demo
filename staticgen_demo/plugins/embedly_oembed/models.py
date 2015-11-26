# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from embedly import Embedly
from jsonfield import JSONField

from .conf import settings


@python_2_unicode_compatible
class EmbedlyOembed(CMSPlugin):
    url = models.URLField(_('URL'), help_text=_('Paste a URL to embed...'))
    data = JSONField(verbose_name=_('Data'), blank=True, null=True)

    class Meta:
        verbose_name = _('embeded content')

    def __str__(self):
        return self.url

    def clean(self):
        self.data = {}
        client = Embedly(settings.EMBEDLY_OEMBED_API_KEY)

        data = client.extract(self.url)
        if 'error' in data:
            return

        self.data = data

    def get_title(self):
        return self.data.get('title', '')

    def get_description(self):
        return self.data.get('description', '')
