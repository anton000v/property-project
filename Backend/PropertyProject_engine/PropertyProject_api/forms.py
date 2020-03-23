from django import forms
from .models import NewBuilding, WayFromMetro
from .widgets import SearchableChoiceWidget, MultipleChoiceWidget
from .utils import generate_slug
from . import choices
from django.core.exceptions import ValidationError
# from django.utils.safestring import mark_safe


class NewBuildingForm(forms.ModelForm):
    # house_letter = forms.ChoiceField(choices=choices.HOUSE_LETTER_CHOICES,)
    slug = forms.SlugField(widget=forms.TextInput(attrs={'readonly': True}), required=False)
    class Meta:
        model = NewBuilding
        fields = '__all__'
        widgets = {
            'district': SearchableChoiceWidget(widget_title="Выберите район"),
            'street' : SearchableChoiceWidget(widget_title='Выберите улицу'),
            'parking' : MultipleChoiceWidget(
            not_comleted_choice=(choices.NOT_COMPLETED)
            ),
        }

    class Media:
            js = ( 'admin/js/PropertyProject_api/micro-districts-filter.js',
                   'admin/js/PropertyProject_api/address-control.js',
                   )

    def clean_slug(self):
        print(self.cleaned_data)
        form_address = "{} {}{}".format(
            self.cleaned_data['street'],
            self.cleaned_data['house_number'],
            self.cleaned_data['house_letter'],
            )
        old_slug = self.cleaned_data['slug']
        new_slug = generate_slug(address=form_address)
        print("SLUG: "+new_slug)
        if new_slug != old_slug:
            if new_slug == 'new':
                raise ValidationError('Slug не может быть "new".')
            if new_slug == '':
                raise ValidationError('Slug не может быть пустым.')
            try:
                building = NewBuilding.objects.get(slug=new_slug)
                # raise ValidationError(mark_safe(('''Такой новострой уже существует.'''
                # <a href="{0}">Открыть</a>''').format(building.get_absolute_url())?
                # ))
                raise ValidationError('Такой новострой уже существует.')
            except NewBuilding.DoesNotExist:
                return new_slug
        else:
            return old_slug

class WayFromMetroForm(forms.ModelForm):
    class Meta:
        model = WayFromMetro
        fields = '__all__'
        widgets = {
            'metroChoices': SearchableChoiceWidget(widget_title="Выберите метро"),
        }
