# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from redactor.widgets import RedactorEditor

from .conf import settings


class TextEditorWidget(RedactorEditor):

    def __init__(self, *args, **kwargs):
        super(TextEditorWidget, self).__init__(*args, **kwargs)
        self.upload_to = ''
        self.allow_file_upload = False
        self.allow_image_upload = False
        self.custom_options = settings.TEXTPLUGIN_REDACTOR_OPTIONS
