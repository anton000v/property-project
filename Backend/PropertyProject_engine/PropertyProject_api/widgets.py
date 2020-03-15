from django import forms

class ChoiceDistrictWidget(forms.widgets.Select):
    template_name = 'admin/PropertyProject_api/widgets/ChoiceDistrict.html'

class ChoiceStreetWidget(forms.widgets.Select):
    template_name = 'admin/PropertyProject_api/widgets/ChoiceDistrict.html'
