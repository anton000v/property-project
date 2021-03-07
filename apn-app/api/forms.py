import logging
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import NewBuilding, WayFromMetro, FlatForSale
from .widgets import SearchableChoiceWidget, MultipleChoiceWidget
from utils.helpers import generate_slug
from . import choices


logger = logging.getLogger(__name__)


class NewBuildingForm(forms.ModelForm):
    slug = forms.SlugField(widget=forms.TextInput(attrs={'readonly': True}), required=False)

    class Meta:
        model = NewBuilding
        fields = '__all__'
        widgets = {
            'district': SearchableChoiceWidget(widget_title="Выберите район"),
            'street': SearchableChoiceWidget(widget_title='Выберите улицу'),
            'developer': SearchableChoiceWidget(widget_title='Выберите застройщика'),
            'parking': MultipleChoiceWidget(
                not_comleted_choice=(choices.NOT_COMPLETED)
            ),
        }

    class Media:
        js = ('admin/js/api/micro-districts-filter.js',
              'admin/js/api/address-control.js'
              )

    def clean(self):
        cleaned_data = super(NewBuildingForm, self).clean()
        street = cleaned_data.get("street")
        house_number = cleaned_data.get("house_number")
        house_letter = cleaned_data.get("house_letter")
        if street and house_number:
            if not house_letter:
                house_letter = ''
            form_address = "{} {}{}".format(street, house_number, house_letter)
            old_slug = cleaned_data.get('slug')
            new_slug = generate_slug(address=form_address)
            # print("SLUG: "+new_slug)
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
                    logger.error('[{}]Попытка создания новостроя {}. Такой новострой существует!'.format(
                        datetime.now().strftime("%d/%m/%Y %H:%M"), new_slug))
                    raise ValidationError('Такой новострой уже существует.')
                except NewBuilding.DoesNotExist:
                    cleaned_data['slug'] = new_slug
            else:
                cleaned_data['slug'] = old_slug
        return cleaned_data


class WayFromMetroForm(forms.ModelForm):
    class Meta:
        model = WayFromMetro
        fields = '__all__'
        widgets = {
            'metro': SearchableChoiceWidget(widget_title="Выберите метро"),
        }


class FlatForSaleForm(forms.ModelForm):
    class Meta:
        model = FlatForSale
        fields = '__all__'
        widgets = {
            'building': SearchableChoiceWidget(widget_title="Выберите дом"),
        }
