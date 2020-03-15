from django import forms
from .models import NewBuilding
from .widgets import ChoiceDistrictWidget, ChoiceStreetWidget
from . import choices

class NewBuildingForm(forms.ModelForm):
    # district = forms.ChoiceField(choices=choices.DISTRICT_CHOICES,
    #                          label=u"Район", initial=choices.NOT_COMPLETED,
    #                          widget=ChoiceDistrictWidget
    #                          )

    class Meta:
        model = NewBuilding
        fields = '__all__'
        widgets = {
            'district': ChoiceDistrictWidget(),
            'street' : ChoiceStreetWidget(),
        }
