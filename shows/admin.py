# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import register

from shows.models import Show, Schedule


@register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("published", "name", "duration")
    list_display_links = ("name", "duration")
    list_filter = ("published", )
    search_fields = ("name", )


@register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("show", "start", "end")
    list_display_links = ("show", "start", "end")
    list_filter = ("start", "end")
    search_fields = ("show__name", )
    raw_id_fields = ("show", )