from django.db import models
from extras.utils import extras_features
from django.core.validators import MinValueValidator, MaxValueValidator

from dcim.fields import ASNField
from ipam.fields import IPNetworkField

# ASN Pool DB Structure
@extras_features("webhooks")
class asnPool(models.Model):
    name = models.CharField(max_length=50)
    first_asn = ASNField()
    last_asn = ASNField()
    tag = models.CharField(max_length=20, default=None, null=True, blank=True)
    pool_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# VNI Pool DB Structure
@extras_features("webhooks")
class vniPoolModel(models.Model):
    name = models.CharField(max_length=50)
    first_vni = models.PositiveIntegerField()
    last_vni = models.PositiveIntegerField()
    tag = models.CharField(max_length=20, default=None, null=True, blank=True)
    pool_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# IP Pool DB Structure
@extras_features("webhooks")
class ipPoolModel(models.Model):
    name = models.CharField(max_length=50)
    subnet = models.CharField(max_length=50)
    tag = models.CharField(max_length=20, default=None, null=True, blank=True)
    pool_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# AOS Blueprint DB Structure
class blueprintModel(models.Model):
    name = models.CharField(max_length=100)
    blueprintId = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# AOS Security Zones (VRFs) DB Structure
class securityZonesModel(models.Model):
    name = models.CharField(max_length=100)
    securityZoneId = models.CharField(max_length=150)
    securityZoneRouteTarget = models.CharField(max_length=100)
    securityZoneLinkedBlueprint = models.ForeignKey(blueprintModel, on_delete=models.CASCADE)
    securityZoneType = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# AOS Virtual Networks DB Structure
class virtualNetworksModel(models.Model):
    name = models.CharField(max_length=100)
    virtualNetworkId = models.CharField(max_length=150)
    virtualNetworkIp = models.CharField(max_length=150)
    virtualNetworkOverlayType = models.CharField(max_length=150)
    virtualNetworkLinkedSecurityZone = models.ForeignKey(securityZonesModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name