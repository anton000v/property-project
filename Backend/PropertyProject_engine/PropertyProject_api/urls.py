from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "property project"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api/find-buildings/',views.FindBuildings.as_view()),
    path('api/get-building/', views.GetBuilding.as_view()),
    path('api/get-micro-districts/', views.MicroDistrictChoices.as_view()),
    path('api/check-address/', views.AddressChecker.as_view()),
    ]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
