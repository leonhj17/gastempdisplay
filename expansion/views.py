# coding:utf-8
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from rest_framework import viewsets

from random import randint

from .models import ExpansionKks, MeasureValue
from .serializers import KksSerializer, MeasureValueSerializer


# Create your views here.
def funview(request):
    a = randint(0, 9)
    b = randint(0, 9)
    return render(request, 'home.html', {
        'a': a,
        'b': b
    })


def addview(request):
    a = request.GET.get('a', '0')
    b = request.GET.get('b', '0')
    c = int(a) + int(b)
    return HttpResponse(c)


def addview2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('expansion:add2', args=(a, b))
    )


class KksViewset(viewsets.ModelViewSet):
    queryset = ExpansionKks.objects.all()
    serializer_class = KksSerializer


class MeasureValueViewset(viewsets.ModelViewSet):
    time = MeasureValue.objects.values('case_time').last()
    # queryset = MeasureValue.objects.filter(case_time=time['case_time'])
    queryset = MeasureValue.objects.filter(**time).filter(kks__vector__in=['z'])
    # queryset = MeasureValue.objects.all()[:10]
    serializer_class = MeasureValueSerializer


def f5_ajax(request):
    f5_dict = [{'a': 1, 'b': 2, 'c': 3}, {'a': 2, 'b': 3, 'c': 4}]
    print u'执行'
    return HttpResponse(json.dumps(f5_dict), content_type='application/json')


def rename_key(item):
    if isinstance(item, dict) and item.get('kks__vector'):
        item[item['kks__vector']] = str(item['value'])
        item['case_time'] = str(item['case_time'])
        del item['kks__vector']
        del item['value']
    return item

def restruct(item):
    if isinstance(item, dict) and item.get('kks__ab'):
        item[item['kks__ab']] = {
            'x': item.get('x', 0),
            'y': item.get('y', 0),
            'z': item.get('z', 0)
        }
        del item['kks__ab']
        del item['x']
        del item['y']
        del item['z']
    return item

def query_vector(request):
    # 查询x，y，z三个方向上膨胀量
    queryx = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'x')

    queryy = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'y')

    queryz = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'z')

    # 字典键值替换
    queryx = map(rename_key, queryx)
    queryy = map(rename_key, queryy)
    queryz = map(rename_key, queryz)

    # 字典合并
    func = lambda dict1, dict2: dict(dict1, **dict2)
    query = map(func, map(func, queryx, queryy), queryz)
    print u'取数'
    print query
    return HttpResponse(json.dumps(query), content_type='application/json')
    # return render(
    #     request, 'expansionbase.html',
    #     {'query': query}
    # )


def query_ab(request):
    query_lx = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'x').filter(kks__ab='left')

    query_ly = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'y').filter(kks__ab='left')

    query_lz = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'z').filter(kks__ab='left')

    query_rx = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'x').filter(kks__ab='right')

    query_ry = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'y').filter(kks__ab='right')

    query_rz = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'z').filter(kks__ab='right')

    query_lx = map(rename_key, query_lx)
    query_ly = map(rename_key, query_ly)
    query_lz = map(rename_key, query_lz)
    query_rx = map(rename_key, query_rx)
    query_ry = map(rename_key, query_ry)
    query_rz = map(rename_key, query_rz)

    func = lambda dict1, dict2: dict(dict1, **dict2)
    query_l = map(func, map(func, query_lx, query_ly), query_lz)
    query_r = map(func, map(func, query_rx, query_ry), query_rz)

    query_l = map(restruct, query_l)
    query_r = map(restruct, query_r)

    query = map(func, query_l, query_r)

    print u'取数'
    print query
    return HttpResponse(json.dumps(query), content_type='application/json')
