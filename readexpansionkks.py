# _*_ encoding:utf-8 _*_
import os
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gastempdisplay.settings')
import datetime
import pytz

import django

django.setup()

from expansion.models import ExpansionKks, Time, MeasureValue

path = os.path.join(os.getcwd(), 'expansionkks.csv')


# 将txt文件转化为列表形式，列表中每一项为字典
def readtxt(filepath):
    result = []
    with open(filepath, 'rb') as f:
        data = csv.reader(f)
        for line in data:
            cell = {}
            # 先找到对应外键，再插入数值
            cell['kks'] = line[0]
            cell['location'] = line[1].decode('gbk')
            cell['ab'] = line[2]
            cell['vector'] = line[3]
            result.append(cell)
    return result


# 批量导入
def add_db(filepath):
    kkslist = []
    data = readtxt(filepath)
    for dic in data:
        kkslist.append(ExpansionKks(**dic))
    ExpansionKks.objects.bulk_create(kkslist)


if __name__ == '__main__':
    add_db(path)
    print 'done'
