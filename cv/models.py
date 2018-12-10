# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Work(models.Model):
  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to='works')
  url = models.URLField(null=True, blank=True)


class Technologie(models.Model):
  name = models.CharField(max_length=50)
  icon = models.CharField(max_length=50)
  progress = models.PositiveSmallIntegerField()
  url = models.URLField(null=True, blank=True)
