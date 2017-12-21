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

def restruct_time(item, time):
    if isinstance(item, dict) and item.get('case_time'):
        item[time] = {
            'case_time': str(item.get('case_time', '0')),
            'value': str(item.get('value', 0))
        }
        del item['case_time']
        del item['value']
    return item

time = MeasureValue.objects.values('case_time').order_by('case_time')
time_iter = 0
time_iter_rl = 0
time_iter_rate = 0


def query_vector(request):
    global time_iter
    # 查询x，y，z三个方向上膨胀量
    queryx = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=time[time_iter]['case_time']
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'x')

    queryy = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=time[time_iter]['case_time']
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'y')

    queryz = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        case_time=time[time_iter]['case_time']
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
    ).filter(kks__vector=u'z')

    # 字典键值替换
    queryx = map(rename_key, queryx)
    queryy = map(rename_key, queryy)
    queryz = map(rename_key, queryz)

    # 字典合并
    func = lambda dict1, dict2: dict(dict1, **dict2)
    query = map(func, map(func, queryx, queryy), queryz)
    print u'取vector'
    time_iter += 100
    print time_iter
    return HttpResponse(json.dumps(query), content_type='application/json')
    # return render(
    #     request, 'expansionbase.html',
    #     {'query': query}
    # )


def query_ab(request):
    global time_iter_rl
    # 按照左右侧查询各个方向膨胀量
    query_lx = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rl]['case_time']
    ).filter(kks__vector=u'x').filter(kks__ab='left')

    query_ly = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rl]['case_time']
    ).filter(kks__vector=u'y').filter(kks__ab='left')

    query_lz = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rl]['case_time']
    ).filter(kks__vector=u'z').filter(kks__ab='left')

    query_rx = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rl]['case_time']
    ).filter(kks__vector=u'x').filter(kks__ab='right')

    query_ry = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rl]['case_time']
    ).filter(kks__vector=u'y').filter(kks__ab='right')

    query_rz = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rl]['case_time']
    ).filter(kks__vector=u'z').filter(kks__ab='right')

    # 修改键值
    query_lx = map(rename_key, query_lx)
    query_ly = map(rename_key, query_ly)
    query_lz = map(rename_key, query_lz)
    query_rx = map(rename_key, query_rx)
    query_ry = map(rename_key, query_ry)
    query_rz = map(rename_key, query_rz)

    # 按左右侧组合膨胀量
    func = lambda dict1, dict2: dict(dict1, **dict2)
    query_l = map(func, map(func, query_lx, query_ly), query_lz)
    query_r = map(func, map(func, query_rx, query_ry), query_rz)

    # 修改数据结构
    query_l = map(restruct, query_l)
    query_r = map(restruct, query_r)

    # 合并左右侧膨胀量
    query = map(func, query_l, query_r)
    time_iter_rl += 100
    print 'time_rl'+str(time_iter_rl)
    print u'取ab'
    return HttpResponse(json.dumps(query), content_type='application/json')


def query_rate(request):
    global time_iter_rate
    query_now = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rate+90]['case_time']
    )

    query_before = MeasureValue.objects.values(
        'kks__location',
        'kks__ab',
        'kks__vector',
        'value',
        'case_time').filter(
        # case_time=MeasureValue.objects.values('case_time').last()['case_time']
        case_time=time[time_iter_rate]['case_time']
    )

    query_now = map(restruct_time, query_now, ['now']*query_now.__len__())
    query_before = map(restruct_time, query_before, ['before']*query_before.__len__())

    func = lambda dict1, dict2: dict(dict1, **dict2)
    query = map(func, query_now, query_before)
    time_iter_rate += 90
    return HttpResponse(json.dumps(query), content_type='application/json')
