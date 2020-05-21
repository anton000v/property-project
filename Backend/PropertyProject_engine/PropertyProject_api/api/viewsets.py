from PropertyProject_api.models import Street, AdministrativeDistrict, Developer, NewBuilding
from .serializer import NewBuildingSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

class NewBuildingFilter(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr='icontains')
    flag = filters.TypedChoiceFilter(choices=BOOLEAN_CHOICES,)
                                            # coerce=strtobool)
    class Meta:
        model = NewBuilding
        fields = {
            'name' : ['icontains']

        }

class NewBuildingViewSet(viewsets.ReadOnlyModelViewSet):
    #list create retrieve update partial_update destroy
    queryset = NewBuilding.objects.all()
    serializer_class = NewBuildingSerializer
    # filter_backends = (DjangoFilterBackend,)
    filterset_class = NewBuildingFilter
    lookup_field = 'slug'