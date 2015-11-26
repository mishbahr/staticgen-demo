# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('caption', models.TextField(verbose_name='Caption', blank=True)),
                ('image', filer.fields.image.FilerImageField(related_name='picture_plugins', verbose_name='Image', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
