[1mdiff --git a/cv/serializers.py b/cv/serializers.py[m
[1mindex a67d727..bb389a6 100644[m
[1m--- a/cv/serializers.py[m
[1m+++ b/cv/serializers.py[m
[36m@@ -3,7 +3,10 @@[m
 [m
 [m
 from rest_framework import serializers[m
[31m-from .models import Work, Technologie, Category[m
[32m+[m[32mfrom rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField[m
[32m+[m
[32m+[m[32mfrom .models import Work, Technologie, Category, GeoPoint[m
[32m+[m
 [m
 class CategorySerializer(serializers.ModelSerializer):[m
 [m
[36m@@ -24,3 +27,11 @@[m [mclass WorkSerializer(serializers.ModelSerializer):[m
     class Meta:[m
         model = Work[m
         fields = '__all__'[m
[32m+[m
[32m+[m
[32m+[m[32mclass GeoPointSerializer(GeoFeatureModelSerializer):[m
[32m+[m
[32m+[m[32m    class Meta:[m
[32m+[m[32m        model = GeoPoint[m
[32m+[m[32m        geo_field = 'geom'[m
[32m+[m[32m        fields = ('name', 'geom')[m
[1mdiff --git a/cv/views.py b/cv/views.py[m
[1mindex 4a37222..3f76afc 100644[m
[1m--- a/cv/views.py[m
[1m+++ b/cv/views.py[m
[36m@@ -4,8 +4,9 @@[m [mfrom __future__ import unicode_literals[m
 from django.shortcuts import render[m
 from rest_framework import viewsets[m
 [m
[32m+[m[32mfrom .serializers import GeoPointSerializer[m
 from .serializers import TechnologieSerializer, WorkSerializer, CategorySerializer[m
[31m-from .models import Technologie, Work, Category[m
[32m+[m[32mfrom .models import Technologie, Work, Category, GeoPoint[m
 [m
 [m
 class CategoryViewSet(viewsets.ModelViewSet):[m
[36m@@ -21,3 +22,8 @@[m [mclass TechnologieViewSet(viewsets.ModelViewSet):[m
 class WorkViewSet(viewsets.ModelViewSet):[m
     queryset = Work.objects.all()[m
     serializer_class = WorkSerializer[m
[32m+[m
[32m+[m
[32m+[m[32mclass GeoPointViewSet(viewsets.ModelViewSet):[m
[32m+[m[32m    queryset = GeoPoint.objects.all()[m
[32m+[m[32m    serializer_class = GeoPointSerializer[m
[1mdiff --git a/cvQuentinRamesREST/urls.py b/cvQuentinRamesREST/urls.py[m
[1mindex 165cec6..4b7aa40 100644[m
[1m--- a/cvQuentinRamesREST/urls.py[m
[1m+++ b/cvQuentinRamesREST/urls.py[m
[36m@@ -16,7 +16,7 @@[m [mIncluding another URLconf[m
 from django.conf.urls import url, include[m
 from django.contrib import admin[m
 from rest_framework import routers[m
[31m-from cv.views import TechnologieViewSet, WorkViewSet, CategoryViewSet[m
[32m+[m[32mfrom cv.views import TechnologieViewSet, WorkViewSet, CategoryViewSet, GeoPointViewSet[m
 from django.conf import settings[m
 from django.conf.urls.static import static[m
 [m
[36m@@ -24,6 +24,7 @@[m [mrouter = routers.DefaultRouter()[m
 router.register(r'categories', CategoryViewSet)[m
 router.register(r'technologies', TechnologieViewSet)[m
 router.register(r'works', WorkViewSet)[m
[32m+[m[32mrouter.register(r'geopoint', GeoPointViewSet)[m
 [m
 [m
 urlpatterns = [[m
