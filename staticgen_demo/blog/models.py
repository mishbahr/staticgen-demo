# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import PlaceholderField
from filer.fields.image import FilerImageField

from .conf import settings


@python_2_unicode_compatible
class Post(models.Model):

    title = models.CharField(
        _('Title'), max_length=255, help_text=_('The post title.'))
    slug = models.SlugField(
        _('slug'), max_length=255, unique=True,
        help_text=_('The name (slug) for the post, used in URLs.'))
    excerpt = models.TextField(_('Excerpt'), blank=True)
    featured_image = FilerImageField(
        verbose_name=_('Featured Image'), blank=True, null=True,
        help_text=_('Featured image for this post'),
        related_name='blog_post_featured_images')

    content = PlaceholderField(
        'post content', related_name='post_content', help_text=_('The post content.'))

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('Author'), related_name='posts',
        help_text=_('The author of the post.'))

    creation_date = models.DateTimeField(
        auto_now_add=True, help_text=_('The post\'s creation time.'))

    publication_date = models.DateTimeField(
        _('Publication date'), default=timezone.now, db_index=True,
        help_text=_('Used in the URL. If changed, the URL will change.'))

    class Meta:
        ordering = ('-publication_date',)
        get_latest_by = 'publication_date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'year': self.publication_date.year,
            'month': self.publication_date.month,
            'day': self.publication_date.day,
            'slug': self.slug
        }
        return reverse('blog:post_detail', kwargs=kwargs)
