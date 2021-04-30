from django.contrib import admin
from .models import blueprintModel, securityZonesModel, virtualNetworksModel


@admin.register(blueprintModel)
class blueprintModelAdmin(admin.ModelAdmin):
    list_display = ("name", "blueprintId")

@admin.register(securityZonesModel)
class securityZonesModelAdmin(admin.ModelAdmin):
    list_display = ("name", "securityZoneId", "securityZoneRouteTarget", "securityZoneLinkedBlueprint", "securityZoneType")

@admin.register(virtualNetworksModel)
class virtualNetworksModel(admin.ModelAdmin):
    list_display = ("name", "virtualNetworkId", "virtualNetworkIp", "virtualNetworkOverlayType", "virtualNetworkLinkedSecurityZone")

