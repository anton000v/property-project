from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
from . forms import NewBuildingForm,TestForm

admin.site.site_header = 'Property-project'
admin.site.unregister(Group)

class DistrictsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.District
       # js = ('admin/test.js',)

class StreetsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Street


class newBuildingsTabularInLine(admin.TabularInline):
    model = models.buildingImages
    extra = 1


class newLayoutsTabularInLine(admin.TabularInline):
    class Meta:
        verbose_name = 'Планировки'
        verbose_name_plural = 'Items i18n'

    model = models.layoutImages
    extra = 1

class WayFromMetroTabularInLine(admin.TabularInline):
    model = models.wayFromMetro
    extra = 1

# class HouseAddressInline(admin.TabularInline):
#     model = models.HouseAddress
#     extra = 1

class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Test
    form = TestForm

class NewBuildingModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'name',
                'street',
                'house_number',
                'house_letter',
                # 'address',
                'administrativeDistrict',
                'district',
                'micro_district',
                'location',
                'developer',
                'theClass',
                'numberOfStoreys',
                'numberOfBuildings',
                'numberOfSectionsOrEntrances',
                'constructionTechnology',
                'wallsType',
                'warming',
                'roomHeight',
                'numberOfApartmentsInTheHouse',
            )
        }),
        ('Типы квартир', {
            'classes': ('grp-open',),
            'fields': (
                ('numberOfOneRoom', 'squareOfOneRoom'),
                ('numberOfTwoRoom', 'squareOfTwoRoom'),
                ('numberOfThreeRoom', 'squareOfThreeRoom'),
                ('numberOfFourRoom', 'squareOfFourRoom'),),
        }),
        (' ', {
            'fields': (
                'numberOfApartmensPerFloor',
                'commercialPremises',

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
                'numberOfParkingSpaces',
                'price',
                'completionDate',
                'description'),
        }),
    )
    inlines = [newBuildingsTabularInLine, newLayoutsTabularInLine, WayFromMetroTabularInLine]
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


    def formfield_for_choice_field(self, db_field, request, **kwargs):
        # if db_field.name == "status":
        #     kwargs['choices'] = (
        #         ('accepted', 'Accepted'),
        #         ('denied', 'Denied'),
        #     )
        #
        #     if request.user.is_superuser:
        #         kwargs['choices'] += (('ready', 'Ready for deployment'),)
        print("FORM_FIELD FOR CHOICE FIELD IS ACTIVATED")
        return super().formfield_for_choice_field(db_field, request, **kwargs)


admin.site.register(models.NewBuilding, NewBuildingModelAdmin)
admin.site.register(models.District, DistrictsModelAdmin)
admin.site.register(models.Street, StreetsModelAdmin)
admin.site.register(models.Test,TestAdmin)
