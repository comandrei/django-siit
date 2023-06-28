from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Curs

class CursSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Curs
        fields = ["nume", "durata", "pret"]