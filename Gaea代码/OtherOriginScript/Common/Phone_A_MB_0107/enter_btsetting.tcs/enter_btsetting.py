from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#A-MB-0107
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)
def enter_btsetting():
    keyevent(HOME, device=DEV2)
    keyevent(HOME, device=DEV2)
    touch(Template('../../../Design/Phone_A_MB_0107/setting_app.png'), device=DEV2)
    swipe([771,709],[771,2100], steps=15, device=DEV2)
    touch_if(Template('../../../Design/Phone_A_MB_0107/setting_connect.png'), device=DEV2)
    touch_if(Template('../../../Design/Phone_A_MB_0107/setting_preferance_setting.png'), device=DEV2)
    touch_if(Template('../../../Design/Phone_A_MB_0107/setting_bt.png'), device=DEV2)
    assert_exists(Template('../../../Design/Phone_A_MB_0107/bt_setting_title.png'), device=DEV2)

keyevent(WAKEUP, device=DEV2)
keyevent(WAKEUP, device=DEV2)
if exists(Template('../../../Design/Phone_A_MB_0107/bt_setting_title.png'), timeout=5, device=DEV2):
    pass
else:
    enter_btsetting()