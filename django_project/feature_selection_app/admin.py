from django.contrib import admin
from models import Doodle
from models import DoodleType

class DoodleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',) 

class DoodleAdmin(admin.ModelAdmin):
    list_display = ('name', 'doodle_date') 
    list_filter = ('name', 'doodle_date')

#Register each model with its associated admin class
admin.site.register(DoodleType, DoodleTypeAdmin)
admin.site.register(Doodle, DoodleAdmin)
