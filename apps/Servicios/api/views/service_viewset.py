from apps.Servicios.api.serializer.service_serializer import ServiceSerializer, ImageServiceSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        service_serializer = self.get_serializer(self.get_queryset(), many = True)
        alquileres = self.get_serializer(self.get_queryset().filter(category_service = 2), many = True)
        trabajos = self.get_serializer(self.get_queryset().filter(category_service = 1), many = True)
        extra_data={
            "Servicios": service_serializer.data,
            "Alquileres": alquileres.data,
            "Trabajos": trabajos.data
        }

        return Response({'message':'Listado de Productos', 'data':extra_data, 'status': True}, status= status.HTTP_200_OK)
    
    def create(self, request):
        print('Hola desde la creacion de servicios')
        service_serializer = self.serializer_class(data=request.data)
        if service_serializer.is_valid():
            print(service_serializer)
            service_serializer.save()
            return Response({'message': 'servicio creado correctamente', 'data': service_serializer.data}, status=status.HTTP_200_OK)
        print(service_serializer.errors)
        #error_message = service_serializer.errors.get('servicio')[0]
        return Response({'message': service_serializer.errors, 'data': None, 'status': False}, status=status.HTTP_400_BAD_REQUEST)
    
class ImageServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ImageServiceSerializer

    def get_queryset(self):
        return super().get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request, *args, **kwargs):
        image_serializer = self.get_serializer(self.get_queryset(), many = True)

        return Response({'message': 'Listado de imagenes referentes', 'data': image_serializer.data, 'status': True})
    
    def create(self, request, *args, **kwargs):
        image_serializer = self.serializer_class(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            return Response({'message': 'imagen referencial creada correctamente', 'data': image_serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': image_serializer.errors, 'data': None, 'status': False}, status=status.HTTP_400_BAD_REQUEST)