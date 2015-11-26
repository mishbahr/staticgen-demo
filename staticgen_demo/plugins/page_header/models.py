# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class PageHeader(CMSPlugin):
    heading = models.CharField(_('Heading'), max_length=255)
    subheading = models.CharField(_('Subheading'), max_length=255, blank=True)
    background_image = FilerImageField(
        verbose_name=_('Background Image'), blank=True, null=True, related_name='page_headers')

    def __str__(self):
        return self.heading
