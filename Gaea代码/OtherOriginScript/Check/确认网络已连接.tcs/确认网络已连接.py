from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)
do_segment(Segment("../../Common/BackHomeView.tcs"))
for _ in range(10):
    if exists(Template("../../Design/statusbar_wifi_good_mark.png"), timeout=3, threshold=0.90) or exists(Template("../../Design/statusbar_wifi_great_mark.png"), timeout=3, threshold=0.90):
        break
else:
    error('__脚本名称: ' + __file__+ 'Check error')
