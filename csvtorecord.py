# _*_ encoding:utf-8 _*_
import csv
import os

row_num = 0
kks_row = []

path = os.getcwd()
record_path = os.path.join(path, 'expansionrecord')

with open('expansionvalue.csv') as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        row_num += 1
        # 读取第一行kks编号
        if row_num == 1:
            row.pop(0)
            kks_row = row
        else:
            '''
            从第一行开始，每一行为一个文件,并以时间命名
            '''
            time = row.pop(0)
            filename = str(row_num - 1) + '.txt'
            with open(os.path.join(record_path, filename), 'w') as value:
                for i in xrange(len(row)):
                    line = kks_row[i] + ';' + row[i] + ';' + time + '\n'
                    value.write(line)
            print '输出第%s个文件' % (row_num - 1)
