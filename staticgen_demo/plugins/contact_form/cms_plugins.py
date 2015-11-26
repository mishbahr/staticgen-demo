# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ContactForm


class ContactFormPlugin(CMSPluginBase):
    model = ContactForm
    name = _('Contact Form')
    render_template = 'plugins/contact_form/default.html'

plugin_pool.register_plugin(ContactFormPlugin)
