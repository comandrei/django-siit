from rest_framework.viewsets import ModelViewSet

from .models import Curs
from .serializers import CursSerializer

class CursViewSet(ModelViewSet):
    queryset = Curs.objects.all()
    serializer_class = CursSerializer