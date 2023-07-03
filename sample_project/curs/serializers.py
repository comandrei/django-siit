from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Curs, Todo

class CursSerializer(ModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"


class TodoSerializer(ModelSerializer):
    camp_dinamic = SerializerMethodField()

    class Meta:
        model = Todo
        fields = "__all__"

    def get_camp_dinamic(self, obj):
        return obj.id ** 2

    