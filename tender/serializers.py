from rest_framework import serializers
from .models import Eoi, Empresa

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Empresa
         fields =['nome_empresa','endereco']


class EoiSerializer(serializers.HyperlinkedModelSerializer):
    empresa_pulicadora = serializers.SlugRelatedField(
            many=False,
            read_only=True,
            slug_field='nome_empresa'
    )

    class Meta:
        model = Eoi
        fields = [
            'id',
            'assunto',
            'descricao',
            'data_pulicacao',
            'data_limite',
            'data_sessao_QA',
            'is_new',
            'empresa_pulicadora',
            'estado_eoi',
        ]
