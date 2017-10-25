# coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from random import randint


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