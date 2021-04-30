from rest_framework.serializers import ModelSerializer
from aisPlugin.models import asnPool
from aisPlugin.models import vniPoolModel
from aisPlugin.models import ipPoolModel
from aisPlugin.models import blueprintModel

class asnPoolSerializer(ModelSerializer):
    class Meta:
        model = asnPool
        fields = ("id", "name", "first_asn", "last_asn", "tag", "pool_id")

class vniPoolModelSerializer(ModelSerializer):
    class Meta:
        model = vniPoolModel
        fields = ("id", "name", "first_vni", "last_vni", "tag", "pool_id")

class ipPoolModelSerializer(ModelSerializer):
    class Meta:
        model = ipPoolModel
        fields = ("id", "name", "subnet", "tag", "pool_id")

class blueprintModelSerializer(ModelSerializer):
    class Meta:
        model = blueprintModel
        fields = ("id", "name", "blueprintId")