from apps.Users.api.serializer import UserSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

    def list(self, request):
        try:
            queryset = self.get_queryset()
            user_serializer = self.get_serializer(queryset, many = True)
            return Response({'message':'listado de correos registrados', 'data': user_serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'error':'ha ocurrido un error en la conexion'}, status=status.HTTP_400_BAD_REQUEST)
        

    def create(self, request):
        print('Here you can create users')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'correo registrado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)
        error_message = serializer.errors.get('email')[0]
        return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)