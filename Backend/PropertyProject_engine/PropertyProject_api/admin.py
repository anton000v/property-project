from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
from . forms import NewBuildingForm, WayFromMetroForm


admin.site.unregister(Group)
admin.site.index_title = 'Панель администратора'
admin.site.site_header = 'Новострои Харькова'
admin.site.site_title = 'Новострои'

class DistrictsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.District

class StreetsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Street


class BuildingImageTabularInline(admin.TabularInline):
    model = models.BuildingImage
    extra = 1
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    # def headshot_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #         )
    #     )


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

class NewBuildingModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'street',
                'house_number',
                'house_letter',
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
        ('Информация о квартирах', {
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
        ('Прочее', {
            'fields': (
                'elevator',
                'parking',
                'number_of_parking_spaces',
                'price',
                'completion_date',
                'description'),
        }),
        ('Системная информация. Заполняется автоматически',{
            'fields' : (
                'slug',
                'lat',
                'lng',
            ),
        }

        )
    )
    inlines = [BuildingImageTabularInline, LayoutImageTabularInLine, WayFromMetroTabularInLine]
    change_list_template="admin/PropertyProject_api/property_change_list.html"
    form = NewBuildingForm

    class Meta:
        model = models.NewBuilding

    class Media:
        css = {
             'all': ('admin/css/PropertyProject_api/admin.css',
             "https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/css/select2.min.css",
             )
        }

        js = (
        # "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/js/bootstrap-select.min.js",
        "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js",
        "https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/js/select2.min.js",
        # "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js",
        # "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/js/bootstrap-select.min.js",
        )

admin.site.register(models.NewBuilding, NewBuildingModelAdmin)
admin.site.register(models.District, DistrictsModelAdmin)
admin.site.register(models.Street, StreetsModelAdmin)
# admin.site.register(models.Test,TestAdmin)
