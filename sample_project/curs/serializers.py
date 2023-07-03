from rest_framework.serializers import ModelSerializer

from .models import Curs, Todo

class CursSerializer(ModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"