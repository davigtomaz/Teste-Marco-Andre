from rest_framework.serializers import ModelSerializer

from garagem.models import Modelo

class ModeloSerializer(ModeloSerializer):
    class Meta: 
        model = Modelo
        fields = "__all__"