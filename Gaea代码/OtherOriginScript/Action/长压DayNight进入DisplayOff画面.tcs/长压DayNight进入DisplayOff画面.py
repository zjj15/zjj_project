from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)
#手顺
#1、长压Hardkey ITSW_DayNight
keyevent(DAY_NIGHT, panel="Preset Switch", mode="CAN", duration=2, device=DEV1)
#keyevent(PRESET_DAY_NIGHT, duration=2, device=DEV1)

sleep(5)