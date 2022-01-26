from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

if exists(Template('../../Design/ShortBar_OnlineVideo_focus.png'), timeout=1, threshold=0.95):
    pass
else:
    do_segment(Segment('../../Screen/迁移到在线视频画面.tcs'))
do_segment(Segment('../../Screen/进入iQIYI设置画面.tcs'))

## logout
if poco('未登录', text='未登录').exists():
    pass
else:
    poco('退出登录', text='退出登录').click()
    #点击‘是’
    poco(text='是').click()
