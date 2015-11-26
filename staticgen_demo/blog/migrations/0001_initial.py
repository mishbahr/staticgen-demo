# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models

from cms.models import PlaceholderField
from filer.fields.image import FilerImageField

from ..conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='The post title.', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(help_text='The name (slug) for the post, used in URLs.', unique=True, max_length=255, verbose_name='slug')),
                ('excerpt', models.TextField(verbose_name='Excerpt', blank=True)),
                ('creation_date', models.DateTimeField(help_text="The post's creation time.", auto_now_add=True)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Used in the URL. If changed, the URL will change.', verbose_name='Publication date', db_index=True)),
                ('author', models.ForeignKey(related_name='posts', verbose_name='Author', to=settings.AUTH_USER_MODEL, help_text='The author of the post.')),
                ('content', PlaceholderField(related_name='post_content', slotname='post content', editable=False, to='cms.Placeholder', help_text='The post content.', null=True)),
                ('featured_image', FilerImageField(related_name='blog_post_featured_images', verbose_name='Featured Image', blank=True, null=True, to='filer.Image', help_text='Featured image for this post')),
            ],
            options={
                'ordering': ('-publication_date',),
                'get_latest_by': 'publication_date',
            },
        ),
    ]
