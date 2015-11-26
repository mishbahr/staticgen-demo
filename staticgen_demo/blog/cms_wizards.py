# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth import get_permission_codename
from django.utils.translation import ugettext_lazy as _

from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import PostCreationForm
from .models import Post


class BlogWizard(Wizard):
    model = Post

    def user_has_add_permission(self, user, **kwargs):
        if not user:
            return False
        if user.is_superuser:
            return True

        opts = self.model._meta
        if user.has_perm('%s.%s' % (opts.app_label, get_permission_codename('add', opts))):
            return True

        # By default, no permission.
        return False

blog_wizard = BlogWizard(
    title=_('New post'),
    weight=200,
    model=Post,
    form=PostCreationForm,
    description=_('Create a new blog post.'),
)

wizard_pool.register(blog_wizard)
