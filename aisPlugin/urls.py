from django.urls import path
from . import views

urlpatterns = [
    path(
        "asn_pools/", 
        views.asnPoolListView.as_view(), 
        name="asnpools_list"
    ),

    path(
        "asn_pools/add/", 
        views.asnPoolCreateView.as_view(), 
        name="asnpools_create"
    ),

    path(
        "asn_pools/delete/",
        views.asnPoolBulkDeleteView.as_view(),
        name="asnpools_bulk_delete",
    ),

    path(
        "asn_pools/<int:pk>/edit/",
        views.asnPoolEditView.as_view(),
        name="asnpools_edit",
    ),
    path(
        "vni_pools/", 
        views.vniPoolListView.as_view(), 
        name="vnipools_list"
    ),

    path(
        "vni_pools/add/", 
        views.vniPoolCreateView.as_view(), 
        name="vnipools_create"
    ),

    path(
        "vni_pools/delete/",
        views.vniPoolBulkDeleteView.as_view(),
        name="vnipools_bulk_delete",
    ),

    path(
        "vni_pools/<int:pk>/edit/",
        views.vniPoolEditView.as_view(),
        name="vnipools_edit",
    ),
    path(
        "ip_pools/", 
        views.ipPoolListView.as_view(), 
        name="ippools_list"
    ),

    path(
        "ip_pools/add/", 
        views.ipPoolCreateView.as_view(), 
        name="ippools_create"
    ),

    path(
        "ip_pools/delete/",
        views.ipPoolBulkDeleteView.as_view(),
        name="ippools_bulk_delete",
    ),

    path(
        "ip_pools/<int:pk>/edit/",
        views.ipPoolEditView.as_view(),
        name="ippools_edit",
    ),
]
