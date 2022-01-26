from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

keyevent(WIRECTR_SOURCE, device=DEV1)

keyevent(ITCMD_OK, device=DEV1)
keyevent(ITCMD_MENU, device=DEV1)


