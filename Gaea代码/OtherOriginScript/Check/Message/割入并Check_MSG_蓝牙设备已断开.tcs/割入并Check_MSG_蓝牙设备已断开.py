from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)

#do_segment(Segment('../../../Common/Phone_A_MB_0107/enter_btsetting.tcs'))
#do_segment(Segment('../../../Common/Phone_S_MB_0569/enter_btsetting.tcs'))

#touch_if(Template('../../../Design/Phone_S_MB_0569/bt_switch_on.png'), timeout=5, device=DEV2)

#touch_if(Template('../../../Design/Phone_A_MB_0107/bt_switch_on.png'), timeout=5, device=DEV2)
for i in range(3):
    flick([757, 34], DIR_DOWN, step=15, speed=SPEED_NORMAL, device=DEV2)
    if exists(Template('../../../Design/Phone_A_MB_0107/bt_statusbar_on.png'), timeout=2, device=DEV2) or exists(Template('../../../Design/Phone_A_MB_0107/bt_statusbar_off.png'), timeout=2, device=DEV2):
        break
touch_if(Template('../../../Design/Phone_A_MB_0107/bt_statusbar_on.png'), timeout=2, device=DEV2)
assert_exists(Template('../../../Design/bt_disconnected.png'), timeout=30, device=DEV1)