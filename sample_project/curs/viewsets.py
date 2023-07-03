from rest_framework.viewsets import ModelViewSet

from .models import Curs, Todo
from .serializers import CursSerializer, TodoSerializer

class CursViewSet(ModelViewSet):
    queryset = Curs.objects.all()
    serializer_class = CursSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
