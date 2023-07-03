from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Curs, Todo

class CursSerializer(ModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"


class TodoSerializer(ModelSerializer):
    feedback = SerializerMethodField()

    class Meta:
        model = Todo
        fields = "__all__"

    def get_feedback(self, obj):
        return f"Feedback pentru {obj.title}"

    