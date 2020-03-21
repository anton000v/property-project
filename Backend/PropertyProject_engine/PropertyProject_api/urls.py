from django.urls import path
from django.contrib import admin
from . import views
app_name = "property project"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api/buildings/', views.NewBuildingView.as_view()),
    path('api/get-micro-districts/', views.MicroDistrictChoices.as_view()),
    path('api/check-address/', views.AddressChecker.as_view()),
    # path('api/update_house_letter_valid_choices', views.UpdateHouseLetterValidChoices.as_view()),
    # path('')
    ]
