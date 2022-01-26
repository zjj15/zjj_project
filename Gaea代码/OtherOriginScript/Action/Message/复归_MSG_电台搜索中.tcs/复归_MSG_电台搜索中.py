from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

if exists(Template("../../../Design/radio_searching.png"), timeout=3, device=DEV1):
    wait_for_disappearance(Template("../../../Design/radio_searching.png"), timeout=25, device=DEV1)