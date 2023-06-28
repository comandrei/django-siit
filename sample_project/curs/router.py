from rest_framework.routers import DefaultRouter
from .viewsets import CursViewSet

router = DefaultRouter()
router.register(r"curs", CursViewSet)
