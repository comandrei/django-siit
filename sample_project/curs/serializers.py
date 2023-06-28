from rest_framework.serializers import ModelSerializer

from .models import Curs

class CursSerializer(ModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"