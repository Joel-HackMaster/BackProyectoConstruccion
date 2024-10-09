from apps.Servicios.models import Service
from rest_framework import serializers
from apps.Servicios.models import ImagesService


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'description', 'image', 'category_service', 'indicator_service')

    def validate_indicator_service(self, value):
        if value is None:
            raise serializers.ValidationError('Tienes que ingresar un descuento, si el producto no cuenta con un descuento asignale 0')
        return value
    
    def validate_name(self, value):
        if value is None:
            raise serializers.ValidationError('El campo name no puede estar en blanco')
        return value
    
    def validate_description(self, value):
        if value is None:
            raise serializers.ValidationError('El campo description no puede estar en blanco')
        return value

    def to_representation(self, instance): #Para obtener los valores toma este metodo
        return {
            'name': instance.name,
            'description': instance.description,
            'image': instance.image,
            'category': instance.category_service.description,
            'discount': instance.indicator_service.descount_value,
        }

class ImageServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesService
        fields = ('description', 'image')

    def to_representation(self, instance):
        return {
            'name': instance.description,
            'image': instance.image
        }

    
