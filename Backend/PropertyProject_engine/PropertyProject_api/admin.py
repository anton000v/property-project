from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
from . forms import NewBuildingForm, WayFromMetroForm
# from django.utils.translation import gettext as _

# admin.site.site_header = 'Property-project'
admin.site.unregister(Group)
admin.site.index_title = 'Панель администратора'
admin.site.site_header = 'Новострои Харькова'
admin.site.site_title = 'Новострои'

class DistrictsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.District
       # js = ('admin/test.js',)

class StreetsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Street


class BuildingImageTabularInline(admin.TabularInline):
    model = models.BuildingImage
    extra = 1
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"


class LayoutImageTabularInLine(admin.TabularInline):
    model = models.LayoutImage
    extra = 1
    verbose_name = "Изображение планировки"
    verbose_name_plural = "Изображения планировок"

class WayFromMetroTabularInLine(admin.TabularInline):
    model = models.WayFromMetro
    form = WayFromMetroForm
    extra = 1
    verbose_name = "Расстояние от метро"
    verbose_name_plural = "Расстояния от метро"

# class HouseAddressInline(admin.TabularInline):
#     model = models.HouseAddress
#     extra = 1

# class TestAdmin(admin.ModelAdmin):
#     class Meta:
#         model = models.Test
#     form = TestForm

class NewBuildingModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'street',
                'house_number',
                'house_letter',
                # 'address',
                'administrative_district',
                'district',
                'micro_district',
                'houising_number',
                'location',
                'developer',
                'the_class',
                'number_of_storeys',
                'number_of_buildings',
                'number_of_sections_or_entrances',
                'construction_technology',
                'walls_type',
                'warming',
                'room_height',
                'number_of_apartments_in_house',
                'slug',
                'lat',
                'lng',
            )
        }),
        ('Типы квартир', {
            'classes': ('grp-open',),
            'fields': (
                ('number_of_one_room', 'square_of_one_room'),
                ('number_of_two_room', 'square_of_two_room'),
                ('number_of_three_room', 'square_of_three_room'),
                ('number_of_four_room', 'square_of_four_room'),),
        }),
        (' ', {
            'fields': (
                'number_of_apartments_per_floor',
                'commercial_premises',

            ),
        }),
        ('Коммуникации', {
            'fields': (
                'heating',
                'gasification',),
        }),
        (' ', {
            'fields': (
                'elevator',
                'parking',
                'number_of_parking_spaces',
                'price',
                'completion_date',
                'description'),
        }),
    )
    inlines = [BuildingImageTabularInline, LayoutImageTabularInLine, WayFromMetroTabularInLine]
    change_list_template="admin/PropertyProject_api/property_change_list.html"
    # change_form_template="admin/PropertyProject_api/change_forms.html"
    # autocomplete_fields = ['street', ]
    form = NewBuildingForm

    # exclude_add = [ 'street', ]

    class Meta:
        model = models.NewBuilding

    class Media:
        css = {
             'all': ('admin/css/PropertyProject_api/admin.css',
             )
        }
        js = ("https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
             "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js",
             "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/js/bootstrap-select.min.js",
             )


    # def formfield_for_choice_field(self, db_field, request, **kwargs):
    #     # if db_field.name == "status":
    #     #     kwargs['choices'] = (
    #     #         ('accepted', 'Accepted'),
    #     #         ('denied', 'Denied'),
    #     #     )
    #     #
    #     #     if request.user.is_superuser:
    #     #         kwargs['choices'] += (('ready', 'Ready for deployment'),)
    #     print("FORM_FIELD FOR CHOICE FIELD IS ACTIVATED")
    #     return super().formfield_for_choice_field(db_field, request, **kwargs)


admin.site.register(models.NewBuilding, NewBuildingModelAdmin)
admin.site.register(models.District, DistrictsModelAdmin)
admin.site.register(models.Street, StreetsModelAdmin)
# admin.site.register(models.Test,TestAdmin)
