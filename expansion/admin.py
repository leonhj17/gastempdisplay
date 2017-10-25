# coding:utf-8
from django.contrib import admin

from .models import Time, ExpansionKks, MeasureValue


# Register your models here.
class TimeAdmin(admin.ModelAdmin):
    list_display = ['case_time']
    list_filter = ['case_time']
    search_fields = ['case_time']


class ExpansionKksAdmin(admin.ModelAdmin):
    list_display = ['kks', 'location', 'ab', 'vector']
    list_filter = ['kks', 'location', 'ab', 'vector']
    search_fields = ['kks', 'location', 'ab', 'vector']


class MeasureValueAdmin(admin.ModelAdmin):
    list_display = ['kks', 'value', 'case_time']
    list_filter = ['kks', 'case_time']
    search_fields = ['kks']

admin.site.register(Time, TimeAdmin)
admin.site.register(ExpansionKks, ExpansionKksAdmin)
admin.site.register(MeasureValue, MeasureValueAdmin)
