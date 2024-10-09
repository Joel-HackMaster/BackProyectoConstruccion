from rest_framework.routers import DefaultRouter
from apps.Users.api.view.user_viewset import UserViewSet


router = DefaultRouter()

router.register(r'user', UserViewSet, basename='users')

urlpatterns = router.urls