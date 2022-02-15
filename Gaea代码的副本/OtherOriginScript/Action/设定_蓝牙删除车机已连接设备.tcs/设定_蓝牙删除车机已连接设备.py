from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

if exists(Template('../../Design/bt_setting_断开.png'), timeout=3, device=DEV1):
    touch_if(Template('../../Design/bt_setting_断开.png'), timeout=3, device=DEV1)
    wait_for_appearance(Template('../../Design/bt_setting_MSG_蓝牙已断开.png'), device=DEV1)
    wait_for_disappearance(Template('../../Design/bt_setting_MSG_蓝牙已断开.png'), device=DEV1)
for i in range(3):
    touch_if(Template('../../Design/bt_setting_btn_删除.png'), device=DEV1, timeout=2)
 
