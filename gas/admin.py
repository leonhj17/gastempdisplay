from django.contrib import admin

# Register your models here.
from .models import Temp


class TempAdmin(admin.ModelAdmin):
    list_display = ['loc_gz', 'loc_umd', 'loc_ab', 'temp', 'case_time']
    list_filter = ['loc_gz', 'loc_umd', 'loc_ab', 'temp', 'case_time']
    search_fields = ['loc_gz', 'loc_umd', 'loc_ab', 'temp']


admin.site.register(Temp, TempAdmin)
