# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from filer.fields.image import FilerImageField


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
        ('filer', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('heading', models.CharField(max_length=255, verbose_name='Heading')),
                ('subheading', models.CharField(max_length=255, verbose_name='Subheading', blank=True)),
                ('background_image', FilerImageField(related_name='page_headers', verbose_name='Background Image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
