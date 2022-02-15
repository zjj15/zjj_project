from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)
touch(Template('../../Design/start_search_btn.png'), timeout=1, device=DEV1)

for i in range(5):
    if exists(Template('../../Design/radio_searching.png'), timeout=1, device=DEV1):
        break
    else:
        pass
else:
    error('Check_BT电话画面 error...')
