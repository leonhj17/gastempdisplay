# _*_ encoding:utf-8 _*_
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gastempdisplay.settings')
import datetime
import pytz

import django

django.setup()

from expansion.models import Time, MeasureValue, ExpansionKks

path = os.path.join(os.getcwd(), 'expansionrecord')


# 将txt文件转化为列表形式，列表中每一项为字典
def readtxt(filepath):
    result = []
    with open(filepath) as f:
        data = f.readlines()
        for line in data:
            cell = {}

            line = line.strip('\n')
            line = line.split(';')
            # 先找到对应外键，再插入数值
            cell['kks'] = ExpansionKks.objects.get(kks=line[0])
            cell['value'] = float(line[1])
            cell['case_time'] = datetime.datetime.strptime(
                line[2], '%a %b %d %H:%M:%S %Y'
            )
            result.append(cell)
    return result


# 批量导入
def add_db(filepath):
    valuelist = []
    data = readtxt(filepath)
    for dic in data:
        valuelist.append(MeasureValue(**dic))
    MeasureValue.objects.bulk_create(valuelist)


if __name__ == '__main__':
    filelist = []
    for root, dirs, files in os.walk(path):
        filelist = files

    for i, filename in enumerate(filelist):
        filepath = os.path.join(path, filename)
        add_db(filepath)
        print '已插入%s文件' % (i + 1)