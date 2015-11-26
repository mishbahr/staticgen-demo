# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.conf import settings

from storages.backends.s3boto import S3BotoStorage


class S3StaticStorage(S3BotoStorage):
    location = settings.AWS_S3_STATIC_FILES_LOCATION


class S3DefaultStorage(S3BotoStorage):
    location = settings.AWS_S3_DEFAULT_FILES_LOCATION
