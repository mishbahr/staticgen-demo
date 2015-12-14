# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.dispatch import receiver
from django.utils import translation

from cms.models import Title
from cms.signals import page_moved, post_publish, post_unpublish

from staticgen.models import Page
from staticgen.staticgen_pool import staticgen_pool
from staticgen.staticgen_views import StaticgenView


class StaicgenDemoStaticViews(StaticgenView):

    def items(self):
        return (
            'django.contrib.sitemaps.views.sitemap',
            'robots.txt',
            'page_not_found',
            'application_error',
        )

staticgen_pool.register(StaicgenDemoStaticViews)


class StaticgenCMSView(StaticgenView):

    def items(self):
        items = Title.objects.public().filter(
            page__login_required=False,
            page__site_id=settings.SITE_ID,
        ).order_by('page__path')
        return items

    def url(self, obj):
        translation.activate(obj.language)
        url = obj.page.get_absolute_url(obj.language)
        translation.deactivate()
        return url

staticgen_pool.register(StaticgenCMSView)


@receiver((page_moved, post_publish, post_unpublish, ))
def mark_cms_page_as_changed(sender, **kwargs):
    page = kwargs['instance']
    language = kwargs['language']

    public_url = page.get_public_url(language=language)
    try:
        page = Page.objects.get(path=public_url)
    except Page.DoesNotExist:
        pass
    else:
        page.publisher_state = Page.PUBLISHER_STATE_CHANGED
        page.save()
