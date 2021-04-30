from rest_framework import routers
from django.conf.urls import include, re_path
from .views import asnPoolViewSet, vniPoolViewSet, ipPoolViewSet

router = routers.DefaultRouter()
router.register(r'asn_pools', asnPoolViewSet)
router.register(r'vni_pools', vniPoolViewSet)
router.register(r'ip_pools', ipPoolViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     re_path('^', include(router.urls)),
# ]
