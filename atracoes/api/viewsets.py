from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filterset_fields = ['id', 'nome', 'descricao']
    filter_backends = [DjangoFilterBackend]

