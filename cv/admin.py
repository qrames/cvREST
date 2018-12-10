# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Technologie, Work


class TechnologieAdmin(admin.ModelAdmin):
    model = Technologie


class WorkAdmin(admin.ModelAdmin):
    model = Work


admin.site.register(Technologie, TechnologieAdmin)
admin.site.register(Work, WorkAdmin)
