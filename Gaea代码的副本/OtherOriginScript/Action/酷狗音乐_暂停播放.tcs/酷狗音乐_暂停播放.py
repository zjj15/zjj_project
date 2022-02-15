from autost.api import *

for i in range(20):
    touch_if(Template('../../Design/OnlienMusic_Play_Button.png'), timeout=1.5)
    touch_if(Template('pic/capture_20210506145326162694.png'), timeout=1.5)
    if not exists(Template('../../Design/OnlienMusic_Play_Button.png'), timeout=1):
        break
    if not exists(Template('pic/capture_20210506145326162694.png'), timeout=1):
        break
else:
    error('OnlineMusic Play Error!')

