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
