from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

if exists(Template('../../../Design/MSG_ClearFavorite.png'), timeout=3, device=DEV1):
    touch_if(Template('../../../Design/clear_no.png'), timeout=3, device=DEV1)
