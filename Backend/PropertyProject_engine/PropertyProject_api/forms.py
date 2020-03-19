from django import forms
from .models import NewBuilding
from .widgets import SearchableChoiceWidget
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
            'district': SearchableChoiceWidget(widget_title="Выберите район"),
            'street' : SearchableChoiceWidget(widget_title='Выберите улицу'),
        }
