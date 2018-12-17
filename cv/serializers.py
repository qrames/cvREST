# -*- coding: utf-8 -*-
# api/serializers.py


from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField

from .models import Work, Technologie, Category, GeoPoint


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TechnologieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technologie
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = '__all__'


class GeoPointSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = GeoPoint
        geo_field = 'geom'
        fields = ('name', 'geom')
