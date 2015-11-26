# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Picture(CMSPlugin):
    image = FilerImageField(
        verbose_name=_('Image'), related_name='picture_plugins')
    caption = models.TextField(_('Caption'), blank=True)

    def __str__(self):
        return self.image.label
