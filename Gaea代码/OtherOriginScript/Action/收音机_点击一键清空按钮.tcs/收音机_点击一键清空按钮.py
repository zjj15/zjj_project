from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)

do_segment(Segment('../../Screen/进入Radio我的收藏画面.tcs'))

touch_if(Template('../../Design/radio_clear_all_favorite_button.png'), device=DEV1, timeout=3)
