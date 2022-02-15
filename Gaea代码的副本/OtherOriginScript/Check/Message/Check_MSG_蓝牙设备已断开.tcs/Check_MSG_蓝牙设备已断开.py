from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'#S-MB-0569
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'#A-MB-0107

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)

do_segment(Segment('../../../Common/Phone_A_MB_0107/enter_btsetting.tcs'))
#do_segment(Segment('../../../Common/Phone_S_MB_0569/enter_btsetting.tcs'))

for i in range(5):
    #touch_if(Template('../../Design/Phone_S_MB_0569/bt_switch_on.png'), timeout=5, device=DEV2)
    touch_if(Template('../../Design/Phone_A_MB_0107/bt_switch_on.png'), timeout=5, device=DEV2)
    if exists(Template('../../Design/bt_disconnected.png'), timeout=30, device=DEV1):
        break
    if not exists(Template('../../Design/statusbar_bt_mark.png'), device=DEV1):
        break
else:
    error('Check_MSG_蓝牙设备已断开 error...')
