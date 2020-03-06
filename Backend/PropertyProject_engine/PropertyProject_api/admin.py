from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

admin.site.site_header = 'My site'
admin.site.unregister(Group)

class DistrictsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Districts
       # js = ('admin/test.js',)

class StreetsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Streets


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
    class Meta:
        model = models.NewBuilding
       # js = ('admin/test.js',)


    # list_display = ('name', 'address', 'district', 'developer',)
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



admin.site.register(models.NewBuilding, NewBuildingModelAdmin)
admin.site.register(models.Districts, DistrictsModelAdmin)
admin.site.register(models.Streets, StreetsModelAdmin)
