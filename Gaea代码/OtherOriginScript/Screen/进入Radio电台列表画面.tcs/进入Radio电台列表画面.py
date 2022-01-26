from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

touch_if(Template('../../Design/radio_tab.png'), timeout=3)
#touch_or(Template('../../Design/tab_radio_list.png'), Template('../../Design/tab_radio_list_selected.png'), timeout=5)
poco('电台列表', text='电台列表', timeout=5).click()
