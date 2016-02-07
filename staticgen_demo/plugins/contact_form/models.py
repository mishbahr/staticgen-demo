# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from requests.api import request
from requests.exceptions import RequestException

HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204


@python_2_unicode_compatible
class ContactForm(CMSPlugin):
    email = models.EmailField(_('Email'))
    hashid = models.CharField(max_length=40, editable=False)

    def __str__(self):
        return self.email

    def clean(self):
        super(ContactForm, self).clean()

        base_url = settings.FWDFORM_API_URL.rstrip('/')
        fwdform_endpoint = '{base_url}/{site_token}/'.format(
            base_url=base_url,
            site_token=settings.FWDFORM_SITE_TOKEN
        )

        payload = {
            'name': 'Contact Form {id}'.format(id=self.pk or ''),
            'recipients': self.email
        }

        if self.hashid:
            payload['hashid'] = self.hashid

        try:
            response = request('post', fwdform_endpoint, data=payload)
            response.raise_for_status()
        except RequestException as e:  # pragma: no cover
            error = e.response.json()
            msg = _('FwdForm Error: {msg}').format(
                msg=error.get('message', _('Something\'s not right.'))
            )
            raise ValidationError(msg)

        if response.status_code == HTTP_201_CREATED:
            data = response.json()
            self.hashid = data.get('hashid', '')
