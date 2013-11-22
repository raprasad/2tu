from django.contrib import admin
from rating.models import Rating

class RatingAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('location__building__name', 'location__name', 'user__last_name', 'user__first_name',)    
    list_display = ('location', 'units', 'user')
admin.site.register(Rating, RatingAdmin)
