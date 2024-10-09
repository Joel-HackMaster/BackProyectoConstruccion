from apps.Servicios.models import CategoryService, Indicator

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        exclude = ('state','created_date', 'deleted_date','modified_date')

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        exclude = ('state','created_date', 'deleted_date','modified_date')