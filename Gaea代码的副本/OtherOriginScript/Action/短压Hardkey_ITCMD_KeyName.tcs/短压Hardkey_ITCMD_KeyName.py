from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__½Å±¾Ãû³Æ: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
key_name = get_param('keyname')
key_name_lower = key_name.lower()

if 'navi' == key_name_lower:
    keyevent(OK, panel='IT Commander', mode='CAN', device=DEV1, channel=CANBUS_CH1)
else:
    error('invalid param')


