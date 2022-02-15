from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

print('待补充')
#do_segment(Segment('../../Action/Message/复归_车机侧挂断BT电话.tcs'))
if not exists(Template('../../Design/statusbar_bt_mark.png'), timeout=2, threshold=0.96):
    do_segment(Segment("../迁移到中控设定画面.tcs"))
    do_segment(Segment("../进入蓝牙设定画面.tcs"))
    ## Spec: Generally, H/U will connect automatically for 3 times within 30s.
    if poco('断开', text='断开', timeout=30).exists():
        pass
    else:
        do_segment(Segment('../../Common/Phone_A_MB_0107/连接车机蓝牙.tcs'))

