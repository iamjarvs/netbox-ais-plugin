import django_tables2 as tables
from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from netbox.views.generic import (
    BulkDeleteView,
    BulkImportView,
    ObjectEditView,
    ObjectListView,
)
from utilities.forms import BootstrapMixin
from utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from .models import asnPool
from .tables import aisAsnTableData
from .models import vniPoolModel
from .tables import aisVniTableData
from .models import ipPoolModel
from .tables import aisIpTableData

"""
ASN Pools
"""
class asnPoolListView(PermissionRequiredMixin, ObjectListView):
    """
    Display ASN Details
    """
    permission_required = "aisPlugin.list_view_asn"
    queryset = asnPool.objects.all()
    table = aisAsnTableData
    template_name = "aisPlugin/asn_pools.html"

class asnPoolForm(BootstrapMixin, forms.ModelForm):
    name = forms.CharField(required=True)
    first_asn = forms.IntegerField(required=True)
    last_asn = forms.IntegerField(required=True)
    tag = forms.CharField(required=False)
    pool_id = forms.CharField(required=True)

    class Meta:
        model = asnPool
        fields = ["name", "first_asn", "last_asn", "tag", "pool_id"]

class asnPoolCreateView(PermissionRequiredMixin, ObjectEditView):
    """
    Display ASN Details
    """
    permission_required = "aisPlugin.create_view_asn"
    queryset = asnPool.objects.all()
    model = asnPool
    model_form = asnPoolForm
    template_name = "aisPlugin/asn_pools_edit.html"
    default_return_url = "plugins:aisPlugin:asnpools_list"

class asnPoolEditView(asnPoolCreateView):
    permission_required = "aisPlugin.edit_asn"

class asnPoolBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """
    Bulk Delete Page
    """
    permission_required = "aisPlugin.bulk_delete_asn"
    queryset = asnPool.objects.all()
    model = asnPool
    table = aisAsnTableData
    default_return_url = "plugins:aisPlugin:asnpools_list"


"""
VNI Pools
"""
class vniPoolListView(PermissionRequiredMixin, ObjectListView):
    """
    Display vni Details
    """
    permission_required = "aisPlugin.list_view_vni"
    queryset = vniPoolModel.objects.all()
    table = aisVniTableData
    template_name = "aisPlugin/vni_pools.html"

class vniPoolForm(BootstrapMixin, forms.ModelForm):
    name = forms.CharField(required=True)
    first_vni = forms.IntegerField(required=True)
    last_vni = forms.IntegerField(required=True)
    tag = forms.CharField(required=False)
    pool_id = forms.CharField(required=True)

    class Meta:
        model = vniPoolModel
        fields = ["name", "first_vni", "last_vni", "tag", "pool_id"]

class vniPoolCreateView(PermissionRequiredMixin, ObjectEditView):
    """
    Display vni Details
    """
    permission_required = "aisPlugin.create_view_vni"
    queryset = vniPoolModel.objects.all()
    model = vniPoolModel
    model_form = vniPoolForm
    template_name = "aisPlugin/vni_pools_edit.html"
    default_return_url = "plugins:aisPlugin:vnipools_list"

class vniPoolEditView(vniPoolCreateView):
    permission_required = "aisPlugin.edit_vni"

class vniPoolBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """
    Bulk Delete Page
    """
    permission_required = "aisPlugin.bulk_delete_vni"
    queryset = vniPoolModel.objects.all()
    model = vniPoolModel
    table = aisVniTableData
    default_return_url = "plugins:aisPlugin:vnipools_list"


"""
IP Pools
"""
class ipPoolListView(PermissionRequiredMixin, ObjectListView):
    """
    Display ip Details
    """
    permission_required = "aisPlugin.list_view_ip"
    queryset = ipPoolModel.objects.all()
    table = aisIpTableData
    template_name = "aisPlugin/ip_pools.html"

class ipPoolForm(BootstrapMixin, forms.ModelForm):
    name = forms.CharField(required=True)
    subnet = forms.CharField(required=True)
    pool_id = forms.CharField(required=True)
    tag = forms.CharField(required=False)

    class Meta:
        model = ipPoolModel
        fields = ["name", "subnet", "tag", "pool_id"]

class ipPoolCreateView(PermissionRequiredMixin, ObjectEditView):
    """
    Display ip Details
    """
    permission_required = "aisPlugin.create_view_ip"
    queryset = ipPoolModel.objects.all()
    model = ipPoolModel
    model_form = ipPoolForm
    template_name = "aisPlugin/ip_pools_edit.html"
    default_return_url = "plugins:aisPlugin:ippools_list"

class ipPoolEditView(ipPoolCreateView):
    permission_required = "aisPlugin.edit_ip"

class ipPoolBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """
    Bulk Delete Page
    """
    permission_required = "aisPlugin.bulk_delete_ip"
    queryset = ipPoolModel.objects.all()
    model = ipPoolModel
    table = aisIpTableData
    default_return_url = "plugins:aisPlugin:ippools_list"