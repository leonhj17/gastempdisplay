# _*_ encoding:utf-8 _*_
import re
import json
dic_gz = {
    u'高过前': 'ggq',
    u'高再前': 'gzq',
    u'高再后': 'gzh'
}

dic_umd = {
    u'上': 'up',
    u'中': 'mid',
    u'下': 'down'
}

dic_ab = {
    u'A': 'a',
    u'B': 'b'
}

jsonfile = []

def readkks():
    with open('gaskks.txt') as f:
        lines = f.readlines()
        pk = 0
        for line in lines:

            pk += 1

            rex_kks = re.compile(r'30HAJ17CT\d{3}')
            rex_gz = re.compile('高过前|高再前|高再后'.decode('utf8'))
            rex_umd = re.compile('上|中|下'.decode('utf8'))
            rex_ab = re.compile('A|B'.decode('utf8'))

            kks = rex_kks.findall(line)
            gz = rex_gz.findall(line.decode('utf8'))
            umd = rex_umd.findall(line.decode('utf8'))
            ab = rex_ab.findall(line.decode('utf8'))
            # print kks[0], dic_gz[gz[0]], dic_umd[umd[0]], dic_ab[ab[1]]

            jsondic = {}
            jsondic['model'] = 'gas.kksdesc'
            jsondic['pk'] = pk
            jsondic['fields'] = {}
            jsondic['fields']['kks'] = kks[0]
            jsondic['fields']['loc_gz'] = dic_gz[gz[0]]
            jsondic['fields']['loc_umd'] = dic_umd[umd[0]]
            jsondic['fields']['loc_ab'] = dic_ab[ab[1]]
            jsonfile.append(jsondic)
    return json.dumps(jsonfile)


if __name__ == '__main__':
    jsonfile = readkks()

    print jsonfile