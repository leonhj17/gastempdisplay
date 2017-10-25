# _*_ encoding:utf-8 _*_
from .models import ExpansionKks, MeasureValue
import xadmin


class ExpansionKksAdmin(object):
    list_display = ['kks', 'location', 'ab', 'vector']
    list_filter = ['kks', 'location', 'ab', 'vector']
    search_fields = ['kks', 'location', 'ab', 'vector']


class MeasureValueAdmin(object):
    list_display = ['kks', 'value', 'case_time']
    list_filter = ['kks', 'case_time']
    search_fields = ['kks', 'case_time']
    data_charts = {
        'MeasureValue': {'title': 'MeasureValue', 'x-field': 'case_time', 'y-field': 'value'}
    }

xadmin.site.register(ExpansionKks, ExpansionKksAdmin)
xadmin.site.register(MeasureValue, MeasureValueAdmin)