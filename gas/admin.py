# _*_ encoding:utf-8 _*_
from django.contrib import admin

# Register your models here.
from .models import Temp, KksDesc


class TempAdmin(admin.ModelAdmin):
    list_display = ['kks', 'temp', 'case_time']
    list_filter = ['kks__loc_gz', 'temp', 'case_time']
    search_fields = ['kks', 'temp']


class KksDescAdmin(admin.ModelAdmin):
    list_display = ['kks', 'loc_gz', 'loc_umd', 'loc_ab']
    list_filter = ['loc_gz', 'loc_umd', 'loc_ab']
    search_fields = ['kks', 'loc_gz', 'loc_umd', 'loc_ab']


admin.site.register(Temp, TempAdmin)
admin.site.register(KksDesc, KksDescAdmin)
