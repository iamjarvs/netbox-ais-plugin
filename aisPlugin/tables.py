import django_tables2 as tables
from utilities.tables import BaseTable, ButtonsColumn, ToggleColumn
from .models import asnPool
from .models import vniPoolModel
from .models import ipPoolModel

edit_button_asn = """
<a href="{% url 'plugins:aisPlugin:asnpools_edit' pk=record.pk %}" class="btn btn-xs btn-warning" title="Edit">
    <i class="mdi mdi-pencil"></i>
</a>
"""

class aisAsnTableData(BaseTable):
    pk = ToggleColumn()
    edit = tables.TemplateColumn(template_code=edit_button_asn)

    class Meta(BaseTable.Meta):
        model = asnPool
        fields = ("pk", "name", "first_asn", "last_asn", "tag", "pool_id", "edit")


edit_button_vni = """
<a href="{% url 'plugins:aisPlugin:vnipools_edit' pk=record.pk %}" class="btn btn-xs btn-warning" title="Edit">
    <i class="mdi mdi-pencil"></i>
</a>
"""

class aisVniTableData(BaseTable):
    pk = ToggleColumn()
    edit = tables.TemplateColumn(template_code=edit_button_vni)

    class Meta(BaseTable.Meta):
        model = vniPoolModel
        fields = ("pk", "name", "first_vni", "last_vni", "tag", "pool_id", "edit")


edit_button_ip = """
<a href="{% url 'plugins:aisPlugin:ippools_edit' pk=record.pk %}" class="btn btn-xs btn-warning" title="Edit">
    <i class="mdi mdi-pencil"></i>
</a>
"""

class aisIpTableData(BaseTable):
    pk = ToggleColumn()
    edit = tables.TemplateColumn(template_code=edit_button_ip)

    class Meta(BaseTable.Meta):
        model = ipPoolModel
        fields = ("pk", "name", "subnet", "tag", "pool_id", "edit")