from autost.api import *

print("__脚本名称: " + __file__)

# WIFI_断开网络连接
for i in range(3):
    if exists(Template('../../Design/statusbar_wifi_good_mark.png'), timeout=3, threshold=0.90) or exists(Template('../../Design/statusbar_wifi_great_mark.png'), timeout=3, threshold=0.88):
        # WIFI_断开网络连接
        swipe([1266,43],[1266,650])
        x, y, w, h = poco('Wi-Fi', text='Wi-Fi').get_attr('rect')
        touch([x+w/2,y-50])
        poco('关闭', text='关闭').click()
        sleep(5)
    else:
        break
else:
    error(__file__+' error')
