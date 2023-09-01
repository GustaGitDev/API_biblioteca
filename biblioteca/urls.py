from rest_framework import routers
from .views import bibliotecaViewSet, livrariaViewSet

router = routers.DefaultRouter()
router.register(r'biblioteca', bibliotecaViewSet)
router.register(r'livraria', livrariaViewSet)
urlpatterns = router.urls