from django.contrib import admin
from django.contrib.gis import admin
from demo_app.models import ZoneType, InterestZone

class ZoneTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class InterestZoneAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'acquisition_date')
    list_filter = ('name', 'acquisition_date')


# Register each model with its associated admin class
admin.site.register(ZoneType, ZoneTypeAdmin)
admin.site.register(InterestZone, InterestZoneAdmin)
