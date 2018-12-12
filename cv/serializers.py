# -*- coding: utf-8 -*-
# api/serializers.py


from rest_framework import serializers
from .models import Work, Technologie, Category

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
