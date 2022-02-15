from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

keyevent(ITCMD_MENU, device=DEV1)
keyevent(ITCMD_MENU, device=DEV1)
sleep(1)
