from django.contrib import admin
from django import forms
from olwidget.admin import GeoModelAdmin
from geopastebin.models import Paste

class PasteAdmin(GeoModelAdmin):
    list_display = ('uuid', 'title', 'created', 'updated', 'semi_private')
    list_filter = ('created', 'updated', 'semi_private')
    search_fields = ('uuid', 'title', 'paste', 'description')
    readonly_fields = ('uuid',)

admin.site.register(Paste, PasteAdmin)
