# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.admin.models import DELETION, LogEntry
from django.contrib.admin.options import get_content_type_for_model
from django.core.urlresolvers import NoReverseMatch, Resolver404, resolve, reverse
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from .models import Post


class RedirectOnDeleteMiddleware(object):
    model = Post

    def is_post_detail_view(self, request):
        try:
            matched_url = resolve(request.path_info)
        except Resolver404:
            return False

        if matched_url and not matched_url.app_name == self.model._meta.app_label \
                and matched_url.url_name == 'post_detail':
            return True

    def process_response(self, request, response):

        if response.status_code != 404:
            return response

        if not self.is_post_detail_view(request):
            return response

        if request.user.is_staff:
            try:
                log_entry = LogEntry.objects.filter(user=request.user).order_by('-pk')[0]
            except IndexError:
                log_entry = None

            if log_entry and log_entry.action_flag == DELETION \
                    and log_entry.content_type_id == get_content_type_for_model(self.model).pk:

                try:
                    redirect_url = reverse('blog:posts_list')
                except NoReverseMatch:
                    redirect_url = '/'

                msg = _('The %(name)s "%(obj)s" was deleted.') % {
                    'name': force_text(self.model._meta.verbose_name),
                    'obj': log_entry.object_repr
                }
                messages.error(request, msg)
                return HttpResponseRedirect(redirect_url)

        return response
