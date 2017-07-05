# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class KksDesc(models.Model):
    kks = models.CharField(max_length=15, blank=False, null=False, verbose_name=u'kks编号', default='kks')
    loc_gz = models.CharField(choices=(('ggq', u'高过前'), ('gzq', u'高再前'), ('gzh', u'高再后')),
                              verbose_name=u'烟温探针位置', blank=False, null=False, max_length=5)
    loc_umd = models.CharField(choices=(('up', u'上'), ('mid', u'中'), ('down', u'下')),
                               verbose_name=u'高度', blank=False, null=False, max_length=15)
    loc_ab = models.CharField(choices=(('a', u'左侧'), ('b', u'右侧')),
                              verbose_name=u'左右侧', blank=False, null=False, max_length=5)

    class Meta:
        verbose_name = u'测点KKS'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.kks


class Temp(models.Model):
    kks = models.ForeignKey(KksDesc, verbose_name=u'kks编号')
    temp = models.FloatField(verbose_name=u'测量温度', max_length=1400, blank=True, null=True)
    case_time = models.DateTimeField(verbose_name=u'测量工况时间')
    #
    class Meta:
        verbose_name = u'测点温度'
        verbose_name_plural = verbose_name


