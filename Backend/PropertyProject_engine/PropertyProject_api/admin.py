from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
from . forms import NewBuildingForm

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


class NewBuildingModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'name',
                'street',
                'house_number',
                'house_letter',
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
    change_form_template="admin/PropertyProject_api/change_forms.html"
    # autocomplete_fields = ['street', ]
    form = NewBuildingForm
    class Meta:
        model = models.NewBuilding

    class Media:
        css = {
             'all': ('admin/css/PropertyProject_api/admin.css',)
        }
        js = ('admin/js/micro-districts-filter.js', )

admin.site.register(models.NewBuilding, NewBuildingModelAdmin)
admin.site.register(models.District, DistrictsModelAdmin)
admin.site.register(models.Street, StreetsModelAdmin)
