from rest_framework.serializers import ModelSerializer

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from garagem.models import Veiculo
    
class VeiculoSerializer(ModelSerializer):
    class Meta: 
        model = Veiculo
        fields = "__all__"
        foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Veiculo
        fields = "__all__"

class VeiculoDetailSerializer(ModelSerializer):

    class Meta: 
        model = Veiculo
        fields = "__all__"
        depth = 2
        foto = ImageSerializer(required=False)

    

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "modelo", "preco"]        