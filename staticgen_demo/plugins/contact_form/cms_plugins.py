# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ContactForm


class ContactFormPlugin(CMSPluginBase):
    model = ContactForm
    name = _('Contact Form')
    render_template = 'plugins/contact_form/default.html'

    def render(self, context, instance, placeholder):
        context = super(ContactFormPlugin, self).render(context, instance, placeholder)
        context.update({
            'action_url': '{base_url}/send/{form_token}/'.format(
                base_url=settings.FWDFORM_API_URL.rstrip('/'),
                form_token=instance.hashid
            )
        })
        return context

plugin_pool.register_plugin(ContactFormPlugin)
