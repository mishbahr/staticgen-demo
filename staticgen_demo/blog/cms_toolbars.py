# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool

from .conf import settings
from .models import Post


@toolbar_pool.register
class BlogToolbar(CMSToolbar):
    model = Post
    watch_models = [Post, ]
    supported_apps = ('blog',)

    def populate(self):
        user = getattr(self.request, 'user', None)
        if not self.is_current_app and not user:
            return

        blog_menu = self.toolbar.get_or_create_menu('blog-app', _('Blog'))
        info = self.model._meta.app_label, self.model._meta.model_name

        has_change_perm = user.has_perm('%s.change_%s' % info)
        has_add_perm = user.has_perm('%s.add_%s' % info)
        has_delete_perm = user.has_perm('%s.delete_%s' % info)
        edit_mode = self.toolbar.edit_mode

        if has_change_perm:
            blog_menu.add_sideframe_item(
                _('Articles List'),
                url=reverse('admin:%s_%s_changelist' % info))

        if has_add_perm:
            blog_menu.add_modal_item(_('Add article'), reverse('admin:%s_%s_add' % info))

        current_post = getattr(self.request, settings.BLOG_POST_IDENTIFIER, None)
        if not current_post:
            return

        if has_change_perm:
            # Add a break in the menu
            blog_menu.add_break()

            blog_menu.add_modal_item(
                _('Edit this article'),
                reverse('admin:%s_%s_change' % info, args=(current_post.pk,)),
                disabled=not edit_mode
            )

        if has_delete_perm:
            # Add a break in the menu
            blog_menu.add_break()

            redirect_url = reverse('blog:posts_list')
            blog_menu.add_modal_item(
                _('Delete this article'),
                reverse('admin:%s_%s_delete' % info, args=(current_post.pk,)),
                on_close=redirect_url,
                disabled=not edit_mode
            )
