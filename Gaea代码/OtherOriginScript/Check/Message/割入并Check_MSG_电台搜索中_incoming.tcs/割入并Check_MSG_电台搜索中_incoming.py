from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)
touch(Template('../../Design/start_search_btn.png'), timeout=1, device=DEV1)
assert_exists(Template('../../Design/radio_searching.png'), timeout=3, device=DEV1)

touch_if(Template('../../Design/Phone_S_MB_0569/Diag_CallBegin.png'), device=DEV2, threshold=0.95)
touch_if(Template('../../Design/Phone_S_MB_0569/BTCalling_hangup_1.png'), timeout=30, device=DEV2)
 
if exists(Template('../../Design/radio_searching.png'), timeout=5, device=DEV1):
    pass
elif exists(Template('../../Design/start_search_btn.png'), timeout=5, device=DEV1):
    pass
else:
    error(__file__ + ' error...')
