from django.contrib import admin
from location.models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class PlaceMapAdmin(LeafletGeoAdmin):
    list_display=('name','location')

class PlaceAdmin(LeafletGeoAdmin):
    list_display = ('name','geom')


admin.site.register(PlaceMap,PlaceMapAdmin)
admin.site.register(Places, PlaceAdmin)


