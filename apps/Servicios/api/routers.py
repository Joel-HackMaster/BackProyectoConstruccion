from rest_framework.routers import DefaultRouter
from apps.Servicios.api.views.service_viewset import ServiceViewSet, ImageServiceViewSet
from apps.Servicios.api.views.general_viewset import IndicatorViewSet, CategoryViewSet



router = DefaultRouter()

router.register(r'servicios', ServiceViewSet, basename='servicios'),
router.register(r'categorias', CategoryViewSet, basename='categorias'),
router.register(r'descuento', IndicatorViewSet, basename='descuento')
router.register(r'images', ImageServiceViewSet, basename='images')

urlpatterns = router.urls