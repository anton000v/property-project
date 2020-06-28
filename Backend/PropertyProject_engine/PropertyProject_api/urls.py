from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .router import router

app_name = "property project"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get-micro-districts/', views.MicroDistrictChoices.as_view()), # for old admin panel js script
    path('api/', include(router.urls)),
    path('api/check-address/', views.AddressChecker.as_view()),
    # path('api/find-buildings/',views.APIFindBuildings.as_view()),
    # path('api/get-building/', views.APIGetBuilding.as_view()),
    path('api/get-streets/', views.APIGetStreetsChoices.as_view()),
    path('api/get-districts/', views.APIGetDistrictsChoices.as_view()),
    path('api/get-administrative-districts/', views.APIGetAdministrativeDistrictsChoices.as_view()),
    path('api/get-saltovka-micro-districts/', views.APIGetSaltovkaMicroDistrictsChoices.as_view()),
    path('api/get-severnaya-saltovka-micro-districts/', views.APIGetSevernayaSaltovkaMicroDistrictsChoices.as_view()),
    path('api/get-saltovka-severnaya-saltovka-db-values/', views.APIGetSaltovkaSevernayaSaltovkaDBValues.as_view()),
    path('api/get-developers/', views.APIGetDevelopersChoices.as_view()),
    path('api/get-metro/', views.APIGetMetroChoices.as_view()),
    path('api/get-classes/', views.APIGetClassChoices.as_view())
    ]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
