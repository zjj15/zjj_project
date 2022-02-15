from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#S-MB-0569
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

do_segment(Segment('../../../Common/Phone_S_MB_0569/enter_btsetting.tcs'))

touch(Template('../../../Design/Phone_S_MB_0569/bt_switch_on.png'), timeout=5, device=DEV2)
#error('割入 MSG_蓝牙设备已断开 error...')
