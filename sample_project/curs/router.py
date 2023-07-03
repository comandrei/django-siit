from rest_framework.routers import DefaultRouter
from .viewsets import CursViewSet, TodoViewSet

router = DefaultRouter()
router.register(r"curs", CursViewSet)
router.register(r"todos", TodoViewSet)
