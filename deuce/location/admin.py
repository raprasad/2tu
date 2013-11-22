from django.contrib import admin
from location.models import Building, Location

class BuildingAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name',)    
    list_display = ('name',)
admin.site.register(Building, BuildingAdmin)


class LocationAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('building__name', 'name', 'user__last_name', 'user__first_name',)    
    list_display = ('building', 'name', 'visible', 'latitude', 'longitude', 'altitude')
    list_filter = ('building',)
admin.site.register(Location, LocationAdmin)
