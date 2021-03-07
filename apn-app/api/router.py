from rest_framework import routers
from .viewsets import NewBuildingViewSet, FlatForSaleViewset


router = routers.DefaultRouter()
router.register('buildings', NewBuildingViewSet, basename='NewBuilding')
router.register('flats', FlatForSaleViewset, basename='FlatForSale')