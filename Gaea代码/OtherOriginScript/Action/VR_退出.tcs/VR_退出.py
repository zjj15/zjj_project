from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

if exists(Template('../../Design/StatusBar_VR_1.png'), timeout=1.5, device=DEV1) or exists(Template('../../Design/StatusBar_VR_2.png'), timeout=1.5, device=DEV1):
    keyevent(ITCMD_MENU, device=DEV1)
    keyevent(ITCMD_MENU, device=DEV1)
    sleep(1)
