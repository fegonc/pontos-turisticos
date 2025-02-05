from rest_framework.serializers import ModelSerializer, SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True)
    endereco_completo = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = "__all__"

    def get_endereco_completo(self, obj):
            return f"{obj.endereco.linha1}, {obj.endereco.linha2}"