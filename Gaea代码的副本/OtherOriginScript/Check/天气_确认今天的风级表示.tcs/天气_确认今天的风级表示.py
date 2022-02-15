from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


poco(pos2 = [1119, 353]).exists()
wind = poco(pos2 = [1119, 353]).get_attr('text')
windRange = wind.split(' ', 1)[1][:-1]
windList = []
if '-' in windRange:
    windList = list(windRange.split('-', 1))
else:
    windList.append(windRange)
# 确认风级在0-17级中
for elem in windList:
    if (int(elem)) in range(0,18):
        print(elem)
        pass
    else:
        error('wrong wind display')
