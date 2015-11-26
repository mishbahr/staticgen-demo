# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedlyOembed',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('url', models.URLField(help_text='Paste a URL to embed...', verbose_name='URL')),
                ('data', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Data')),
            ],
            options={
                'verbose_name': 'embeded content',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
