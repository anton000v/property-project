from .viewsets import NewBuildingViewSet, FlatForSaleViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('buildings', NewBuildingViewSet, basename='NewBuilding')
router.register('flats', FlatForSaleViewset, basename='FlatForSale')