# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

from .models import Text
from .widgets import TextEditorWidget


class TextPluginForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'
        widgets = {
            'body': TextEditorWidget(),
        }
