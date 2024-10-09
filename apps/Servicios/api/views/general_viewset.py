from apps.Servicios.api.serializer.general_serializer import CategorySerializer, IndicatorSerializer
from apps.Servicios.models import CategoryService, Indicator
from rest_framework import viewsets, status
from rest_framework.response import Response

class CategoryViewSet(viewsets.GenericViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self, category=None):
        if category is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(state = True, description = category)
    
    def list(self, request):
        data_filter = self.get_queryset()
        data_serializer_all = self.get_serializer(data_filter, many = True)
        return Response({
            'mensaje': 'Listado Categorias',
            'categorias': data_serializer_all.data
            }, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'categoria registrada', 'data': serializer.data}, status=status.HTTP_200_OK)


class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def list(self, request):
        data_filter = self.get_queryset()
        data_serializer = self.get_serializer(data_filter, many = True)
        return Response(data_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'categoria registrada', 'data': serializer.data}, status=status.HTTP_200_OK)
