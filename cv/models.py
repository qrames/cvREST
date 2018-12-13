# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from colorful.fields import RGBColorField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = RGBColorField()

    def __unicode__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='works')
    url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Technologie(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    progress = models.PositiveSmallIntegerField()
    url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.name


class GeoPoint(models.Model):
    name = models.CharField(max_length=200)
    geom = models.GeometryField()
