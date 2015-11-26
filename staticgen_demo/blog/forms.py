# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.api import add_plugin
from cms.utils import permissions

from .models import Post


class PostCreationForm(forms.ModelForm):
    content = forms.CharField(
        label=_('Content'),
        help_text=_('Optional — If supplied, will be automatically added '
                    'within a new text plugin.'),
        required=False, widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', )

    def save(self, commit=True):

        post = super(PostCreationForm, self).save(commit=False)
        # Set owner to current user
        post.author = self.user

        # If 'content' field has value, create a TextPlugin with same and add
        # it to the PlaceholderField
        content = self.cleaned_data.get('content', '')
        if content and permissions.has_plugin_permission(
                self.user, 'TextPlugin', 'add'):

            # If the post has not been saved, then there will be no
            # Placeholder set-up for this article yet, so, ensure we have saved
            # first.
            if not post.pk:
                post.save()

            if post and post.content:
                add_plugin(
                    placeholder=post.content,
                    plugin_type='TextPlugin',
                    language=self.language_code,
                    body=content,
                )

        if commit:
            post.save()

        return post
