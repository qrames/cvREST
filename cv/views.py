# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import GeoPointSerializer
from .serializers import TechnologieSerializer, WorkSerializer, CategorySerializer
from .models import Technologie, Work, Category, GeoPoint


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TechnologieViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all()
    serializer_class = TechnologieSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class GeoPointViewSet(viewsets.ModelViewSet):
    queryset = GeoPoint.objects.all()
    serializer_class = GeoPointSerializer
