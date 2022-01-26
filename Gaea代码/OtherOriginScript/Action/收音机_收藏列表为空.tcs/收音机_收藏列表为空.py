from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print("__脚本名称: " + __file__)
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Screen/进入Radio电台列表画面.tcs'))
touch_or(Template('../../Design/radio_tab_favorite.png'), Template('../../Design/radio_tab_favorite_selected.png'), timeout=5)

do_segment(Segment('../收音机_点击一键清空按钮.tcs'))
touch_if(Template('../../Design/radio_clear_ok.png'), timeout=3, device=DEV1)
