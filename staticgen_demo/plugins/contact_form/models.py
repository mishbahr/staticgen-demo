# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


@python_2_unicode_compatible
class ContactForm(CMSPlugin):
    email = models.EmailField(_('Email'))

    def __str__(self):
        return self.email
