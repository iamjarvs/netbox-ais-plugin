from rest_framework.viewsets import ModelViewSet
from aisPlugin.models import asnPool, vniPoolModel, ipPoolModel, blueprintModel
from .serializers import asnPoolSerializer, vniPoolModelSerializer, ipPoolModelSerializer, blueprintModelSerializer

class asnPoolViewSet(ModelViewSet):
    queryset = asnPool.objects.all()
    serializer_class = asnPoolSerializer

class vniPoolViewSet(ModelViewSet):
    queryset = vniPoolModel.objects.all()
    serializer_class = vniPoolModelSerializer

class ipPoolViewSet(ModelViewSet):
    queryset = ipPoolModel.objects.all()
    serializer_class = ipPoolModelSerializer

class blueprintViewSet(ModelViewSet):
    queryset = blueprintModel.objects.all()
    serializer_class = blueprintModelSerializer