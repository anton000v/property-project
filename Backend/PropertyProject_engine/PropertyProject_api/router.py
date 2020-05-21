from .viewsets import NewBuildingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('buildings', NewBuildingViewSet, basename='NewBuilding')
    