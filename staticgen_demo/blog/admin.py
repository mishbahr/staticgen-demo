# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Post


class PostAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', )
    list_filter = ('author', )
    search_fields = ('title', 'slug', 'author__first_name',  'author__last_name',)
    prepopulated_fields = {'slug': ('title', )}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'publication_date',
                       'excerpt', 'author', 'featured_image', ),
        }),

    )

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        qs = qs.select_related()
        return qs


admin.site.register(Post, PostAdmin)
