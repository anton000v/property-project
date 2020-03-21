from django import forms
from .models import NewBuilding, Test
from .widgets import SearchableChoiceWidget
from . import choices


class TestForm(forms.ModelForm):
    # rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    CH = [(k,k) for k in rus_alphabet]
    choice = forms.ChoiceField(choices=CH)
    # choice = forms.CharField(widget=forms.Select(choices=CHOICES))
    # choice = forms.CharField(max_length=3,
    #         widget=forms.Select(choices=CHOICES))
    # added = forms.CharField(max_length=50)
    # a = forms.CharField(max_length=10)
    class Meta:
        model = Test
        fields = '__all__'
        # widgets = {
        # 'choice' : forms.Select()
        # }

    # def clean(self):
    #     choice = self.data["choice"]
    #     print(choice)
    #     self.fields['choice'].choices = [(choice, choice)]
    #     # print(self.request)
    #     cleaned_data = super(TestForm, self).clean()
        # return cleaned_data

class NewBuildingForm(forms.ModelForm):

    # address = forms.ModelChoiceField(queryset=HouseAddress.objects.all(), empty_label="(Nothing)")
    house_letter = forms.ChoiceField(choices=choices.HOUSE_LETTER_CHOICES)
    class Meta:
        model = NewBuilding
        fields = '__all__'
        widgets = {
            'district': SearchableChoiceWidget(widget_title="Выберите район"),
            # 'address' : AddressChoiceWidget(widget_title="Выберите адресс")
            'street' : SearchableChoiceWidget(widget_title='Выберите улицу'),
            # 'house_letter' : forms.Select(),
        }

    class Media:
            js = ( 'admin/js/PropertyProject_api/micro-districts-filter.js',
                   'admin/js/PropertyProject_api/address-control.js',
                   )

    # def clean_house_letter(self):
    #     print("CLEAN House LETTER METHOD IS ACTIVATED")
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['house_letter'].choices = [('-', 'Без буквы')]
    #     print("__init__ is ACTIVATED!!!")
    #
    # def clean(self):
    #     self.fields['house_letter'].choices = [('-','-'),]
    #     # print(self.fields['house_letter'].choices)
    #
    #     cleaned_data = super().clean()
        # if value in EMPTY_VALUES:
        #     value = u''
        # value = smart_unicode(value)
        # if value == u'':
        #     return value
        # valid_values = set([smart_unicode(k) for k, v in self.choices])
        # if value not in valid_values:
        #     raise ValidationError(ugettext(u'Select a valid choice. That choice is not one of the available choices.'))
        # else:
        #     value = self._choices[int(value)][1]
        # return cleaned_data
