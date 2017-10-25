# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ExpansionKks(models.Model):
    kks = models.CharField(max_length=15, blank=False, null=False, verbose_name=u'膨胀指示器KKS', default='kks')
    location = models.CharField(max_length=20, blank=False, null=False, verbose_name=u'膨胀指示器位置', default=u'水冷壁')
    ab = models.CharField(choices=(('right', u'右侧'), ('left', u'左侧'), ('middle', u'中部')), verbose_name=u'左右侧',
                          blank=False, null=False, max_length=10)
    vector = models.CharField(choices=(('x', u'X方向'), ('y', u'Y方向'), ('z', u'Z方向')),
                              verbose_name=u'方向', blank=False, null=False, max_length=5)

    class Meta:
        verbose_name = u'膨胀指示器描述'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.kks


class Time(models.Model):
    case_time = models.DateTimeField(verbose_name=u'测量时间')

    class Meta:
        verbose_name = u'膨胀测量时间'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return unicode(self.case_time)


class MeasureValue(models.Model):
    kks = models.ForeignKey(ExpansionKks, verbose_name=u'膨胀指示器KKS')
    value = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'实测膨胀量')
    case_time = models.ForeignKey(Time, verbose_name=u'测量时间')

    class Meta:
        verbose_name = u'膨胀实测值'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.value

